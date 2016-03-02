      Program matrix
      Real, Dimension(3)::V
      real, dimension(2,3)::A
      real, dimension(2)::W
      Integer:: i,j

      A=reshape ((/1.0,2.0,3.0,4.0,5.0,6.0/),(/2,3/))
      V = (/1.0,2.0,3.0/)

      DO i=1,2
      w(i)=0.0
      DO j=1,3
      W(i)=w(i)+a(i,j)*v(j)
      end do
      end do
      print*, W
      end program matrix

