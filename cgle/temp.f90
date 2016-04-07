      subroutine forward(output, spacial, xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Complex*8, dimension(xlength),intent(in)::spacial!input array, spacial domain
      Complex*8, dimension(xlength),intent(out)::output!output array, frequency domain
      integer*4::j
      
      do j=1,xlength
      output(j)=spacial(j)*5.
      end do

      end subroutine forward
      

!Do an inverse fast fourier transform
      subroutine back(Inverse,frequency,xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Integer*4::n!used to iterate over the array
      Complex*8, dimension(xlength),intent(in)::frequency!input array, frequency domain
      Complex*8, dimension(xlength),intent(out)::inverse!output array, spacial domain
      do n=1,xlength
      inverse(n)=frequency(n)/5.      
      end do
      end subroutine back
      
      
      subroutine fb(output,oldstate,xlength)
      implicit none
      integer*4, intent(in)::xlength
      complex*8, dimension(xlength), intent(in)::oldstate
      complex*8, dimension(xlength), intent(out)::output
      complex*8, dimension(xlength)::temp
      external :: back, forward
      call forward(temp, oldstate, xlength)
      call back(output, temp, xlength)
      end subroutine fb










 
      
      
!Do a fast fourier transform
      subroutine fft(fftout, spacial, xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Complex*8, dimension(xlength),intent(in)::spacial!input array, spacial domain
      Complex*8, dimension(xlength),intent(out)::fftout!output array, frequency domain
      Integer*4::a,b!used to itterate over the array

      do b=1,xlength
      fftout(b)=0
      end do
      
      do b=1,xlength
      do a=1,xlength
      fftout(b)=fftout(b)+spacial(a)*EXP(real(b-1.)*real(a-1.))!FFT of the input array
      end do
      end do
      end subroutine fft
      
      
!Do an inverse fast fourier transform
      subroutine fftinv(Inverse,frequency,xlength)
      Implicit none
      Integer*4,intent(in)::xlength!length of the input/output array
      Complex*8, dimension(xlength),intent(in)::frequency!input array, frequency domain
      Complex*8, dimension(xlength),intent(out)::inverse!output array, spacial domain
      Complex*8, dimension(xlength)::temp!output array, spacial domain
      Integer*4::n,k!used to iterate over the array
      
      
      do n=1,xlength
      temp(n)=0
      end do
      
      
      do n=1,xlength
      do k=1,xlength
      temp(n)=temp(n)+frequency(k)*EXP(real(k-1.)*real(n-1.))
      end do
      inverse(n)=temp(n)/real(xlength)!inverse fourier transform
      end do
      end subroutine fftinv
            

      subroutine fftinvfft(output,oldstate,xlength)
      implicit none
      integer*4, intent(in)::xlength
      complex*8, dimension(xlength), intent(in)::oldstate
      complex*8, dimension(xlength), intent(out)::output
      complex*8, dimension(xlength)::temppp
      external :: fft, fftinv
      call fft(temppp, oldstate, xlength)
      call fftinv(output, temppp, xlength)
      end subroutine fftinvfft


