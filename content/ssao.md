Title: Screen Space Ambient Occlusion
Author: CpCd0y
Date: 2016-02-01 13:05
Category: Article
Slug: ssao
lang: en
tags: ssao, opengl, rendering

In the real-time rendering field we have always strived for better looking
rendering, if not for a more realistic one. Even so, it is not always a physically based rendering that we are doing.
Thus we often have to "approximate" and fake an effect in order to achieve the sacred 30-60 frames per
second goal.

In this article, I will present to you a method used in many video games
nowadays. This method was first introduced in Crysis (2007) by Vladimir Kajalin
at Crytek.

SSAO is a way to add more depth to a scene by darkening areas where light is
less accessible. This is in opposition with methods of local illumination like
the Phong shading, because SSAO depends on the scene geometry.
It does so by approximating Ambient Occlusion,
which itself is an approximation of global illumination techniques.

<center><img width="400" alt="left: ssao off, right: ssao on" src="https://electronicmeteor.files.wordpress.com/2011/12/ssao-compare1.jpg">
<figcaption>- Left: SSAO OFF, Right: SSAO ON</figcaption></center>

First, I will be presenting the math behind this, and after this, I'll be
explaining a possible implementation.

Enough talking, let's dive into the main subject.

##Rendering Equation

To understand ambient occlusion itself, we need to know where it comes from.

Below is the formula of the rendering equation which is a model introduced in
1986, that generalises a variety of known rendering algorithms.
It tells us that the radiance
leaving a point in a specific direction is the sum of what that point is emitting and any incoming radiance coming toward that same point.

<center>
$L(x \rightarrow \Theta) = L_e(x \rightarrow \Theta) + \int_{\Omega}f_r(x,\Psi \leftrightarrow \Theta)L_i(x \leftarrow
\Psi)cos \Psi d\omega_\Psi$
</center>

$L_e$ being the emitted radiance at $x$, $f_r$ the Bidirectionnal Reflectance
Distribution Function (BRDF, for example: Blinn-Phong or Cook-Torrance) and $L_i$ the
incoming radiance from any direction. The integral is over an hemisphere
$\Omega$ oriented by the surface normal $n$. The $cos \Psi$ is a
weighting term depending on the angle of the incoming ray.

Let's simplify the equation to meet our needs.

We'll assume that the scene uses only a diffuse model so that all the emitted light $L_e$
is coming from another source (environment map or something else). This gives
us : $L_e(x \rightarrow \Theta) = 0$. This removes the left term of the sum, so
we have :

<center>
$L(x \rightarrow \Theta) = \int_{\Omega}f_r(x,\Psi \leftrightarrow \Theta)L_i(x \leftarrow
\psi)cos \Psi d\omega_\Psi$
</center>

Now, let's choose a BRDF. For simplicity's reason, we'll use Lambert's
model, so $f_r(x, \psi \leftrightarrow \Theta) = \frac{c}{\pi}$, with $c$ the
surface color.

Now we get :
<center>
$L(x \rightarrow \Theta) = \frac{c}{\pi}\int_{\Omega}L_i(x \leftarrow
\psi)cos \Psi d\omega_\Psi$
</center>

Because $f_r$ is a constant, we can put it outside the integral.

###Ambient Occlusion

Now, we are getting closer to the ambient occlusion general formula.

We can now, simplify $L_i$ as a simple visibility function $V$ which only
outputs $1$ or $0$ depending on if the point $x$ is visible or not in the
direction $\omega$.

Also, we set $c = 1$, because we assume that the surface is fully reflective,
so the value $1$ won't affect the color. After this, the equation becomes :

<center>
$L(x \rightarrow \Theta) = A_x = \frac{1}{\pi} \int_{\Omega} V_{x, \omega}(n \cdot \omega)d\omega$
</center>

This is the equation giving the occlusion $A$ at a point $x$. We integrate a
visibility function $V$ over a surface normal ($n$) oriented hemisphere ($\omega$)
weighted by the surface's solid angle.

The problem here, is that if we want to compute the visibility function $V$, we
need to cast rays from $x$ and test for intersection with other geometry.
Raytracing is a very computationally expensive process and we cannot usually
afford it for a real-time usage.

Rather than doing full raytracing, we use some tricks in screen space to
approximate this.

##A Screen Space Method

SSAO is one these methods used for approximation ambient occlusion in
real-time.

First let's explain the term "screen space".

Screen space methods are a class of rendering techniques that only use the
information contained in the current (or even the previous) frame. That is, we
compute for each frame, several buffers containing information on each
fragments on the screen. These information usually are, position, normal and
depth of each fragments. In OpenGL, we call this a G-buffer.

<center><img width="400" alt="gbuffer" src="/images/gbuffer.jpg">
<figcaption>- G-buffer: Top left: color buffer, Top right: normals, Bottom left: position buffer, Bottom right: texture coordinates (uv coords)</figcaption></center>

###The idea

The idea of SSAO is to compute an occlusion value at each fragment in screen
space that we store in a SSAO buffer. Each texel's value of this buffer is eventually used to compute the ambient light color.

To compute the occlusion value, we take points distributed in a sphere that a reprojected in screen space so that we can sample the depth buffer.

<center><img width="300" alt="ssao sphere samples" src="/images/ssao_sphere_samples.png">
<figcaption>- SSAO sphere samples</figcaption></center>

Then, we have to check the position of the sampled depth relative to the point
in the sphere. If the latter is inside the geometry, which means it is farther
in the depth buffer than the sampled depth, then this point will contribute to
the ambient occlusion factor.

One problem is that on flat surfaces, like walls, we would have half of the
sphere samples inside the geometry and it would generate false occlusion.

<center><img width="320" alt="ssao sphere samples" src="https://0fps.files.wordpress.com/2013/07/ssao.jpg">
<figcaption>- SSAO buffer: False occlusion, especially on walls and flat surfaces</figcaption></center>

That's why in Crysis, the walls and flat surfaces are darker than they should
be.

To counter this, we'll be using normal-oriented hemispheres. The per-fragment
normals will be sampled from the normal buffer.

As we can see from the picture below, the hemisphere has less samples inside
the geometry, this means less points contributing to the occlusion factor. This
will help in not darkening too much the scene.

<center><img width="300" alt="ssao sphere samples" src="https://mtnphil.files.wordpress.com/2013/06/twotypes.png">
<figcaption>- Sphere sampling vs Hemisphere sampling</figcaption></center>

Then, we'll need to disbrute the few points inside the hemisphere in a particular way. The fact that we'll take only a few points will introduce a banding effect, where 'lines' tend to appear on the surface of objetcs.

<center><img width="500" alt="ssao spheresamples"src="/images/banding.png">
<figcaption>- Banding appears on the grass</figcaption></center>

We can remove this effect by randomly rotation the hemisphere around the
Z-axis for each fragment.

Finally randomly rotating the hemisphere causes noise to appear, which can be
removed via geometry-aware blur.

That's it for the general idea. Let's implement this.

##Implementation

###G-buffer

Before computing SSAO, we need to setup some input info to our shader. As was
said before, we need linear depth, as well as normals and position.
We'll be using MRTs (multiple render targets) to achieve the creation of the 3
buffers at once.

Let's begin with the position buffer.

For the positions, we only get the result of the classic model view projection
product of matrices. So the current fragment's color value would be:

```glsl
    //FragPos is the gl_Position from the vertex shader
    gPositionDepth.xyz = fragPos;
```

For the normals, we first compute the inverse transpose of the model view matrix then multiply it with the actuel normal of the current vertex.

Why do we need this step ? It's because, when a transformation is applied to a
model, it might be non-uniform (only to one axis and not the others), which
deforms the model. If we do not "bend" the normals with this process, we'll
have normal that are not correct. (more info on that <a
href="http://web.archive.org/web/20120228095346/http://www.arcsynthesis.org/gltut/Illumination/Tut09%20Normal%20Transformation.html#d0e9336)">here</a>)

<center><img width="400" alt="ssao sphere samples" src="/images/CircleNormalScaling.svg">
<figcaption>- Normal scale (left), normals not correctly bent (center), normals bent (right) </figcaption></center>

The vertex shader would be:

```glsl
    mat3 normalMatrix = transpose(inverse(mat3(view * model)));
    //Final normal
    Normal = normalMatrix * normal;
```


In the fragment shader, we simply have:

```glsl
    //Normal is the input Normal (see above)
    gNormal = normalize(Normal);
```

Finally, we need the linear depth. We know that depth is linear in view
position (which makes sense), but after the projection process, the depth
becomes non-linear so we need to linearize it again.

To do so, we first get back from the range $[0, 1]$ to Normalized Device Coordinates (NDC) in clip space in the range $[-1, 1]$ and apply the inverse equation that was applied on the depth with the
projection matrix. 

So in the fragment shader we do this:

```glsl
//Put your values in here
const float NEAR = -1.0f;
const float FAR = 1000.0f;
float LinearizeDepth(float depth)
{
    //Back to NDC
    float z = depth * 2.0 - 1.0;
    //Back to linear depth
    return (2.0 * NEAR * FAR) / (FAR + NEAR - z * (FAR - NEAR));
}
```
And finally, juste after, in the main, we have:

```glsl
void main()
{
    gPositionDepth.xyz = FragPos;
    //We linearize the depth of the current fragment
    gPositionDepth.a = LinearizeDepth(gl_FragCoord.z);
    gNormal = normalize(Normal);
}
```
So, now we have completly setup our g-buffer.

###Hemisphere samples distribution

Now that we have our G-buffer, we need to compute pseudo-random points
coordinates in the hemisphere. We want to distribute our points in such a way
that they are more densely packed toward the origin of the hemisphere and
contained only in the unit hemishpere region. This way, the samples closer to
the origin contribute more than the farthest samples.

<center><img width="350" alt="ssao sphere samples"src="./images/fig5.jpg">
<figcaption>- Points distribution in the unit hemisphere</figcaption></center>

We will precompute these samples in a buffer before starting the rendering, and
then we'll send them to the shader as a uniform variable.

Let's use the tools provided by the STL:

```CPP
  std::uniform_real_distribution<GLfloat> randomFloats(0.0, 1.0);
  std::default_random_engine generator;
  //The final result
  std::vector<glm::vec3> ssaoKernel;
```

Now, we have to vary $x$ and $y$ in tangent space in the range $[-1, 1]$, and
$z$ in the range $[0, 1]$. $z$ goes only in this range, because using $[-1, 1]$
will generate sample points for a sphere and not a hemisphere.

Generating 32 samples sounds good:

```CPP
	#define KERNEL_SAMPLES 32
	for (GLuint i = 0; i < KERNEL_SAMPLES; ++i)
	{
		//We generate a random float and get it back in NDC, except for the Z-axis
		glm::vec3 sample(randomFloats(generator) * 2.0 - 1.0, randomFloats(generator) * 2.0 - 1.0, randomFloats(generator));
		//The result is normalized as it needs to fit inside a unit hemisphere
		sample = glm::normalize(sample);
		//Scale the samples to distribute them within the hemisphere
		sample *= randomFloats(generator);

		//Accelerate the samples' falloff (above figure) using this interpolation function
		GLfloat scale = GLfloat(i) / KERNEL_SAMPLES;

		scale = lerp(0.1f, 1.0f, scale * scale);
		sample *= scale;

		//Store the final result
		ssaoKernel.push_back(sample);
	}
```

###The noise texture

We need to generate a 4x4 noise texture to rotate the previously generated
hemisphere along the z-axis.

Using the previous tools, we can generate vectors in NDC. So we only vary the $x$
and $y$ coordinates to rotate on $z$:

```CPP
	std::vector<glm::vec3> ssaoNoise;
	for (GLuint i = 0; i < 16; i++)
	{
		//x and y in NDC
		glm::vec3 noise(randomFloats(generator) * 2.0 - 1.0, randomFloats(generator) * 2.0 - 1.0, 0.0f);
		//Store the final result
		ssaoNoise.push_back(noise);
	}
```

Here's an example of a generated noise texture using the above method :

<center><img width="100" alt="ssao sphere samples" src="/images/X4IUDQW.png">
<figcaption>- 4x4 noise texture </figcaption></center>

Using a 4x4 only texture, we can produce high-frequency noise that we can remove using geometry-aware blur.

Now that we have setup our inputs to the shader, we can start the real implementation.

###SSAO Shader

We first need to create the vertex shader. The SSAO effect is just a screen
space effect, so it's just a quad (square made of 2 triangles) that we're going to use it the same way as position, normal or depth texture.

So, we just setup buffers containing a quad's vertices and uv coordinates, like
this :

```CPP
  //Vertices coordinates
  static const GLfloat quad_vertices[] =
  {
    -1.0f, 1.0f, 0.0f,
    -1.0f, -1.0f, 0.0f,
    1.0f, 1.0f, 0.0f,
    1.0f, -1.0f, 0.0f,
  };
  
  //UV coordinates
  static const GLfloat quad_uvs[] =
  {
    0.0f, 1.0f,
    0.0f, 0.0f,
    1.0f, 1.0f,
    1.0f, 0.0f,
  };
```

These buffer are then used in VBOs in a VAO, that will be giving data to the
vertex shader.

The vertex shader is a follow :

```glsl
layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;

out vec2 TexCoords;

void main()
{
  gl_Position = vec4(position, 1.0f);
  TexCoords = texCoords;
}
```

It maps our quad coordinates in screen space, as it was given in input.

After this, we need to retrieve the position, depth, normal and the noise
textures from the fragment shader. We also need the sample kernel we computed
above. Finally, we need the projection matrix.

Let's get into the fragment shader.

As said before, we'll sample the different textures:


```glsl
  //Sample the Position (xyz) and linear depth (w)
  vec3 fragPos = texture2D(gPositionDepth, TexCoords).xyz;
  //Sample normal
  vec3 normal = texture2D(gNormal, TexCoords).rgb;
  vec3 randomVec = texture2D(texNoise, TexCoords * noiseScale).xyz;
```

noiseScale is defined a such :

```glsl
  const vec2 noiseScale = vec2(screen_width / noise_texture_width, screen_height / noise_texture_height); 
```

Next, we need to compute the basis that will help us project the hemisphere sample points. To create this "tripod" matrix we need to get the normal, tangent and bitangent of the current point.
We already have the normalized normal in tangent space from the normal texture. To get the tangent, we need to do this :

```glsl
  vec3 tangent = normalize(randomVec - normal * dot(randomVec, normal));
```

Now, getting the bitangent is extremely easy, because we have the normal and
its tangent:

```glsl
  vec3 bitangent = cross(normal, tangent);
```

Finally, we create the basis that is going to transform the samples for a unit
hemisphere space to the local frame view space along the current normal.

```glsl
  //The TBN name comes from Tangent Bitangent Normal
  mat3 TBN = mat3(tangent, bitangent, normal);
```

The above process is done using the Gram-Schmidt process.

After this, we iterate through the samples of the kernel. And, for each sample
point in the hemisphere, we project it along the surface normal using the TBN matrix, then we scale the sample by a radius and place the sample at the position sampled from the position texture.

```glsl
    vec3 sample = TBN * samples[i];
    sample = fragPos + sample * radius;
```

Then, we reproject the sample with the projection matrix to get its coordinates
in screen space and we do the usual perspective divide and transform the final
result from NDC to the $[0; 1]$ range :

```glsl
    vec4 offset = vec4(sample, 1.0);
    //Project to screen space
    offset = projectionMatrix * offset;
    //Perspective divide
    offset.xyz /= offset.w;
    //Back from NDC
    offset.xyz = offset.xyz * 0.5 + 0.5;
```

Now, we can to sample our linear depth buffer and check if the current sample
(sample) is under the geometry (sampleDepth). If it is the case, then the
current sample contributes to the AO, otherwise, it doesn't. Also, we introduce
a range check to ensure that the sample is in fact inside the hemisphere we are
using and avoid contribution from too far away samples.

```glsl
    //Sample linear depth
    float sampleDepth = texture2D(gPositionDepth, offset.xy).z;
    //Range check to avoid contribution from too far away samples
    float rangeCheck = smoothstep(0.0, 1.0, radius / abs(fragPos.z -
      sampleDepth));
    //Add contribution to the AO term
    occlusion += (sampleDepth >= sample.z ? 1.0 : 0.0)  * rangeCheck;
```

Finally, outside the loop, we scale the occlusion term by the number of samples
(KERNEL_SIZE) and substract the result from 1.0 to get a usable value because
we have to remember that the value (occlusion) we computed is a <b>contribution</b> factor and we want its "darkening" factor equivalent.

So, we juste have :

```glsl
  occlusion = 1.0 - (occlusion / KERNEL_SIZE);
```

With all of this, we get this result :

<center><img width="1000" alt="ssao spheresamples"src="/images/SSAO_ON-OFF.png">
<figcaption>- Result: before (left), after (right). Also, the position, ssao,
normal and albedo textures are shown</figcaption></center>
