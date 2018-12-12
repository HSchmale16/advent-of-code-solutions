program day11
    implicit none
    
    integer, dimension(1:300,1:300) :: grid, res 
    integer :: i, x, y, serialNum, cmax, maxx, maxy, maxi
    real :: start, finish

    read(*,*) serialNum

    call cpu_time(start)
    do x = 1, 300
        do y = 1, 300
            grid(x,y) = (x + 10) * y + serialNum
            grid(x,y) = grid(x,y) * (x + 10)
            grid(x,y) = MOD(grid(x,y), 1000) / 100 - 5
        end do
    end do
    
    res = 0
    maxi = 0 
    cmax = 0
    do i = 0, 299
        do y = 1, 300 - i
            do x = 1, 300 - i
                res(x,y) = res(x,y) + sumOuter(grid, x, y, i) 
                if (res(x,y) .gt. cmax) then
                    cmax = res(x,y)
                    maxi = i
                    maxx = x
                    maxy = y
                end if 
            end do
        end do
        ! i is off by 1 since we are making a grid size by blah
        if (i .eq. 2) then 
            write(*,*) "Part 1 = ", maxx, maxy, cmax
        end if 
    end do  
    
    write(*,*) "Part 2 = ", maxx, maxy, maxi + 1, cmax
    call cpu_time(finish)

    write(*,*) "Cpu Time = ", finish - start

contains
    ! Assumes res is passed back in each time, and n in counted up from the beginning.
    ! x and y are the top left coord 
    function sumNxN(g, x, y, n) result(s)
        integer :: g(1:300, 1:300), x, y, n, s 
    
        !> slightly optimized solution, compared to manually summing, just use a slice.
        !> Allows the compiler to generate very vectorized code
        s = sum(g(x:x+n,y:y+n))
    end function sumNxN

    function sumOuter(g, x, y, n) result(s)
        integer :: g(1:300, 1:300), x, y, s, n 

        s = sum(g(x+n,y:y+n-1)) + sum(g(x:x+n,y+n)) 
    end function sumOuter

end program day11
