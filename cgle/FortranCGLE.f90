!functions in this module:
!arr2arr(othervar,array)
!nextstep(timestep,numtimesteps,A,B,C,D,oldstate)
!nonlinear(timestep,C,D,oldstate)
!fft(spacial)
!fftinv(frequency)


!I need to put it in a module so I can apply functions/subroutines inside other functions/subroutines.
module cgle
contains
!This is just to check I know how to make arrays
      subroutine arr2arr(arrout,othervar,array,arrsize)
      real*4, intent(in)::othervar!some real number
      integer*4, intent(in)::arrsize!The size of the input/output array
      Complex*8, dimension(arrsize),intent(in)::array!The input array
      complex*8,dimension(arrsize),intent(out)::arrout!The output array
      integer*4::i!used to loop through the array
      do i=1,arrsize
      arrout(i)=array(i)+othervar!I am just adding a constant to each number of the complex list.
      end do
      arrout=arrout*5
      return
      end subroutine arr2arr
      
      
      
      
!Create an array as a waveform progresses in time - this is very dodge at the moment.
      subroutine nextstep(timestep,numtimesteps,A,B,C,D, &
      oldstate,xlength,matrixout)
      Implicit none
      real*4, intent(in)::timestep!How large is each timestep
      Integer*4,intent(in)::xlength,numtimesteps!length of input array, number of timesteps (total time =numtimesteps*timestep)
      complex*8, dimension(numtimesteps,xlength),intent(out)::matrixout!output matrix
      Complex*8, dimension(xlength),intent(in)::oldstate!Input matrix
      COMPLEX*8,intent(in)::A,B,C,D!A,B,C,D used in the CGLE



      COMPLEX*8::power,exponential!Used to make understanding the maths below easier
      complex*8, dimension(xlength)::nonlin,fourier,temp,matrixrow !nonlinear term, fourier transform term, intermittant term, the ith row of the matrix
      integer*4::k,t,j !Used to iterate over lists
      
      do j=1,xlength
      matrixrow(j)=oldstate(j)
      end do
      
      
      !This is the initial time row in the array
      do j=1,xlength
      matrixout(1,j)=matrixrow(j)
      end do
      
      
      do t=2,numtimesteps
      
      call nonlinear(nonlin,timestep,C,D,matrixrow,xlength)!getting the effect of the nonlinear term
      call FFT(fourier,nonlin,xlength)!taking the fourier transform acting on the above
      power=-B*timestep*3.14159**2/xlength**2!This is only half the power. the other half is below, in the actual exponential.
      do k=1,xlength
      exponential=EXP(power*(k-1)**2+A*timestep)
      temp(k)=exponential*fourier(k)!Taking the derivative in the frequency domain
      end do
      call FFTinv(matrixrow,temp,xlength)!Going from the frequency domain back to the spacial domain
      
      
      
!      do j=1,xlength
!      matrixout(t,j)=matrixrow(j)!Putting this row onto the output matrix

!      matrixout(t,j)=oldstate(j)!Testing the above line of code for matrixout
!      end do
      end do
      return
      end subroutine nextstep
      
      
      
!Doing the nonlinear term of the CGLE
      subroutine nonlinear(nonlinout,timestep,C,D,oldstate,xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of input/output array
      Integer*4::i!used to iterate over the array
      Complex*8, dimension(xlength),intent(in)::oldstate!the input array
      Complex*8, dimension(xlength),intent(out)::nonlinout!the output array
      COMPLEX*8,intent(in)::C,D!complex numbers used in the CGLE
      Complex*8::power!Used to make calculations easier
      real*4,intent(in)::timestep!Length of a timestep
      
      
      do i=1,xlength
      power=C*ABS(oldstate(i))**2+D*ABS(oldstate(i))**4
      nonlinout(i)=EXP(power*timestep)*oldstate(i)
      !the effect of the nonlinear term
      end do
      return
      end subroutine nonlinear
      
      
      subroutine fftinvfft(output,oldstate,xlength)
      implicit none
      integer*4, intent(in)::xlength
      complex*8, dimension(xlength), intent(in)::oldstate
      complex*8, dimension(xlength), intent(out)::output
      complex*8, dimension(xlength)::temp
      external :: fft, fftinv
      call fft(temp, oldstate, xlength)
      call fftinv(output, temp, xlength)
      return
      end subroutine fftinvfft      
      
      
!Do a fast fourier transform
      subroutine fft(fftout, spacial, xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Integer*4::j,k!used to itterate over the array
      Complex*8, dimension(xlength),intent(in)::spacial!input array, spacial domain
      Complex*8, dimension(xlength),intent(out)::fftout!output array, frequency domain
      complex*8::power!used to make calculations easier
      power=-2*3.14159*COMPLEX(0.,1.)/xlength
      do k=1,xlength
      do j=1,xlength
      fftout(k)=fftout(k)+spacial(j)*EXP(power*(k-1)*(j-1))!FFT of the input array
      end do
      end do
      return
      end subroutine fft
      
      
      
      
!Do an inverse fast fourier transform
      subroutine fftinv(Inverse,frequency,xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Integer*4::n,k!used to iterate over the array
      Complex*8, dimension(xlength),intent(in)::frequency!input array, frequency domain
      Complex*8, dimension(xlength),intent(out)::inverse!output array, spacial domain
      Complex*8::power!used to make calculations easier
      power=2.*3.14159*COMPLEX(0.,1.)/xlength
      do n=1,xlength
      do k=1,xlength
      inverse(n)=inverse(n)+frequency(k)*EXP(power*(k-1)*(n-1))
      end do
      inverse(n)=inverse(n)/xlength!inverse fourier transform
      end do
      return
      end subroutine fftinv
      
      

      
      
end module cgle




