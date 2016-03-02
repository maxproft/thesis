      program circle
      real r, area
!c This program reads a number r and prints
!c the area of the circle which has this radius.
!c This is how you write comments
      write(*,*) 'Give radius r:'
      read(*,*) r
      area = 3.14159*r*r
      write(*,*) 'Area = ', area
      stop
      end program circle
