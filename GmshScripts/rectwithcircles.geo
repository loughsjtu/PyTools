SetFactory("OpenCASCADE");

dx=1.00000;
w =20.00000;
h =8.00000;
Point (1)={0.0,0.0,0.0,dx};
Point (2)={  w,0.0,0.0,dx};
Point (3)={  w,  h,0.0,dx};
Point (4)={0.0,  h,0.0,dx};

Line (1)={1,2};
Line (2)={2,3};
Line (3)={3,4};
Line (4)={4,1};

Circle ( 5)={6.10935,4.79339,0.0,2.58534,0.0,2*Pi};
Circle ( 6)={11.15129,2.75751,0.0,1.99995,0.0,2*Pi};
Circle ( 7)={14.73281,4.92095,0.0,1.64550,0.0,2*Pi};
Circle ( 8)={17.72451,2.21910,0.0,1.67175,0.0,2*Pi};
Circle ( 9)={2.21780,2.10845,0.0,1.60386,0.0,2*Pi};

Line Loop( 1)={1,2,3,4};
Plane Surface( 1)={1};

Line Loop( 2)={  5};
Plane Surface( 2)={  2};

Line Loop( 3)={  6};
Plane Surface( 3)={  3};

Line Loop( 4)={  7};
Plane Surface( 4)={  4};

Line Loop( 5)={  8};
Plane Surface( 5)={  5};

Line Loop( 6)={  9};
Plane Surface( 6)={  6};

BooleanDifference(7) = { Surface{1}; Delete;}{Surface{ 2};Surface{ 3};Surface{ 4};Surface{ 5};Surface{ 6};Delete; };
Physical Surface ("box")={ 7};

Line Loop( 8)={ 5};
Plane Surface ( 8)={ 8};
Physical Surface ("circle1 ")={ 8};

Line Loop( 9)={ 6};
Plane Surface ( 9)={ 9};
Physical Surface ("circle2 ")={ 9};

Line Loop(10)={ 7};
Plane Surface (10)={10};
Physical Surface ("circle3 ")={10};

Line Loop(11)={ 8};
Plane Surface (11)={11};
Physical Surface ("circle4 ")={11};

Line Loop(12)={ 9};
Plane Surface (12)={12};
Physical Surface ("circle5 ")={12};

Physical Line("left") = {2};
Physical Line("right") = {3};
Physical Line("bottom") = {1};
Physical Line("top") = {4};
