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
      real, intent(in)::othervar!some real number
      integer, intent(in)::arrsize!The size of the input/output array
      Complex, dimension(arrsize),intent(in)::array!The input array
      complex,dimension(arrsize),intent(out)::arrout!The output array
      integer::i!used to loop through the array
      do i=1,arrsize
      arrout(i)=array(i)+othervar!I am just adding a constant to each number of the complex list.
      end do
      arrout=arrout*5
      return
      end subroutine arr2arr
      
      
      
      
!Create an array as a waveform progresses in time - this is very dodge at the moment.
      subroutine nextstep(matrixout,timestep,numtimesteps,A,B,C,D, &
      oldstate,xlength)
      Implicit none
      real, intent(in)::timestep!How large is each timestep
      Integer,intent(in)::xlength,numtimesteps!length of input array, number of timesteps (total time =numtimesteps*timestep)
      integer::k,t,j !Used to iterate over lists
      complex, dimension(xlength,numtimesteps),intent(out)::matrixout!output matrix
      Complex, dimension(xlength),intent(in)::oldstate!Input matrix
      complex, dimension(xlength)::nonlin,fourier,temp,matrixrow!nonlinear term, fourier transform term, intermittant term, the ith row of the matrix
      COMPLEX,intent(in)::A,B,C,D!A,B,C,D used in the CGLE
      COMPLEX::power,exponential!Used to make understanding the maths below easier
      
      
      matrixrow=oldstate
      !This is the initial time row in the array
      do j=1,xlength
      matrixout(j,1)=matrixrow(j)
      end do
      
      
      do t=2,numtimesteps
      
      call nonlinear(nonlin,timestep,C,D,matrixrow,xlength)!getting the effect of the nonlinear term
      call FFT(fourier,nonlin,xlength)!taking the fourier transform acting on the above
      power=-B*timestep*3.14159265**2/xlength**2!This is only half the power. the other half is below, in the actual exponential.
      do k=1,xlength
      exponential=EXP(power*(k-1)**2+A*timestep)
      temp(k)=exponential*fourier(k)!Taking the derivative in the frequency domain
      end do
      call FFTinv(matrixrow,temp,xlength)!Going from the frequency domain back to the spacial domain
      
      do j=1,xlength
      matrixout(j,t)=matrixrow(j)!Putting this row onto the output matrix
      end do
      end do
      return
      end subroutine nextstep
      
      
      
      
!Doing the nonlinear term of the CGLE
      subroutine nonlinear(nonlinout,timestep,C,D,oldstate,xlength)
      Implicit none
      Integer,intent(in)::xlength!length of input/output array
      Integer::i!used to iterate over the array
      Complex, dimension(xlength),intent(in)::oldstate!the input array
      Complex, dimension(xlength),intent(out)::nonlinout!the output array
      COMPLEX,intent(in)::C,D!complex numbers used in the CGLE
      Complex::power!Used to make calculations easier
      real,intent(in)::timestep!Length of a timestep
      
      
      do i=1,xlength
      power=C*ABS(oldstate(i))**2+D*ABS(oldstate(i))**4
      nonlinout(i)=EXP(power*timestep)*oldstate(i)
      !the effect of the nonlinear term
      end do
      return
      end subroutine nonlinear
      
      
      
      
!Do a fast fourier transform
      subroutine fft(fftout, spacial, xlength)
      Implicit none
      Integer,intent(in)::xlength!length of the input/output array
      Integer::j,k!used to itterate over the array
      Complex, dimension(xlength),intent(in)::spacial!input array, spacial domain
      Complex, dimension(xlength),intent(out)::fftout!output array, frequency domain
      complex::power!used to make calculations easier
      power=-2*3.1415926*COMPLEX(0.,1.)/xlength
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
      Integer,intent(in)::xlength!length of the input/output array
      Integer::n,k!used to iterate over the array
      Complex, dimension(xlength),intent(in)::frequency!input array, frequency domain
      Complex, dimension(xlength),intent(out)::inverse!output array, spacial domain
      Complex::power!used to make calculations easier
      power=2*3.1415926*COMPLEX(0.,1.)/xlength
      do n=1,xlength
      do k=1,xlength
      inverse(n)=inverse(n)+frequency(k)*EXP(power*(k-1)*(n-1))
      end do
      inverse(n)=inverse(n)/xlength!inverse fourier transform
      end do
      return
      end subroutine fftinv

end module cgle




