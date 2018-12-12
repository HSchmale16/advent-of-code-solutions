program day11
    implicit none
    
    integer, dimension(1:300,1:300) :: grid, res 
    integer :: i, x, y, j, serialNum, cmax, maxx, maxy, maxi

    read(*,*) serialNum

    do x = 1, 300
        do y = 1, 300
            grid(x,y) = (x + 10) * y + serialNum
            grid(x,y) = grid(x,y) * (x + 10)
            grid(x,y) = MOD(grid(x,y), 1000) / 100 - 5

        end do
    end do

    maxi = 0 
    cmax = 0
    do i = 0, 299
        do y = 1, 300 - i
            do x = 1, 300 - i
                j = sumNxN(grid, x, y, i)
                if (j .gt. cmax) then
                    cmax = j
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
     

contains
    ! Assumes res is passed back in each time, and n in counted up from the beginning.
    ! x and y are the top left coord 
    function sumNxN(g, x, y, n) result(s)
        integer :: g(1:300, 1:300), x, y, i, j, s, n 
        
        s = 0
        do i = 0, n
            do j = 0, n
                s = s + g(x+j,y+i)
            end do
        end do 
    end function sumNxN



end program day11
