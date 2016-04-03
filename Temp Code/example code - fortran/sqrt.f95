      real function norm(x,y,z)
      Real:: x,y,z,total
      norm = sqrt(x**2+y**2+z**2)
      total = x+y+z
      end function norm

      program absolute
      real :: a,b,c
      real, external:: norm
      a=1.0
      b=2.0
      c=-2.0
      print*, norm(a,b,c)
      end program absolute
