      real function circlearea(r)
      real:: r
      circlearea = 3.14159*r*r
      write(*,*) "circlearea"
      end function circlearea



      subroutine arr2arr(array,arrsize,arrout,othervar)
      real, intent(in)::othervar
      integer, intent(in)::arrsize
      integer::i
      Complex, dimension(arrsize),intent(in)::array
      complex,dimension(arrsize),intent(out)::arrout
      do i=1,arrsize
      arrout(i)=array(i)+othervar
      end do
      arrout=arrout*5
      return
      end subroutine arr2arr
      
      

      subroutine nextstep(matrixout,timestep,numtimesteps,A,B,C,D, &
      oldstate,xlength)
      Implicit none
      real, intent(in)::timestep

      Integer,intent(in)::xlength,numtimesteps
      integer::k,t


      complex, dimension(xlength,numtimesteps),intent(out)::matrixout

      Complex, dimension(xlength),intent(in)::oldstate
      complex, dimension(xlength)::nonlin,fourier,temp,matrixrow

      COMPLEX,intent(in)::A,B,C,D
      COMPLEX::power,exponential


      
      call nonlinear(nonlin,timestep,C,D,oldstate,xlength)
      call FFT(fourier,nonlin,xlength)
      power=-B*timestep*3.14159265**2/xlength**2
      
      do t=1,numtimesteps

      do k=1,xlength
      exponential=EXP(power*(k-1)**2+A*timestep)
      temp(k)=exponential*fourier(k)
      end do
      call FFTinv(matrixrow,temp,xlength)
      
      do k=1,xlength
      matrixout(j,t)=matrixrow(k,t)
      end do
      return
      
      contains


      
      subroutine nonlinear(nonlinout,timestep,C,D,oldstate,xlength)
      Implicit none
      Integer,intent(in)::xlength
      Integer::i
      Complex, dimension(xlength),intent(in)::oldstate
      Complex, dimension(xlength),intent(out)::nonlinout
      COMPLEX,intent(in)::C,D
      Complex::power
      real,intent(in)::timestep
      do i=1,xlength
      power=C*ABS(oldstate(i))**2+D*ABS(oldstate(i))**4
      nonlinout(i)=EXP(power*timestep)
      end do
      return
      end subroutine nonlinear



      subroutine fft(fftout, spacial, xlength)
      Implicit none
      Integer,intent(in)::xlength
      Integer::i,k
      Complex, dimension(xlength),intent(in)::spacial
      Complex, dimension(xlength),intent(out)::fftout
      complex::power
      power=-2*3.1415926*COMPLEX(0.,1.)/xlength
      do k=1,xlength
      do i=1,xlength
      fftout(k)=fftout(k)+spacial(i)*EXP(power*(k-1)*(i-1))
      end do
      end do
      return
      end subroutine fft


      subroutine fftinv(Inverse,frequency,xlength)
      Implicit none
      Integer,intent(in)::xlength
      Integer::n,k
      Complex, dimension(xlength),intent(in)::frequency
      Complex, dimension(xlength),intent(out)::inverse
      Complex::power
      power=2*3.1415926*COMPLEX(0.,1.)/xlength
      do n=1,xlength
      do k=1,xlength
      inverse(n)=inverse(n)+frequency(k)*EXP(power*(k-1)*(n-1))
      end do
      inverse(n)=inverse(n)/xlength
      end do
      return
      end subroutine fftinv


      end subroutine nextstep



