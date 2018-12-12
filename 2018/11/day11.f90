program day11
    implicit none
    integer, dimension(1:300,1:300) :: grid, g3x3
    integer :: i, x, y, j, serialNum, cmax, maxx, maxy

    read(*,*) serialNum

    do x = 1, 300
        do y = 1, 300
            grid(x,y) = (x + 10) * y + serialNum
            grid(x,y) = grid(x,y) * (x + 10)
            grid(x,y) = MOD(grid(x,y), 1000) / 100 - 5

        end do
    end do
    
    cmax = 0
    do x = 2, 299
        do y = 2, 299
            i = sum3x3(grid, x, y)
            if (i .gt. cmax) then
                cmax = i
                maxx = x
                maxy = y
            end if 
        end do
    end do
   
    write(*,*) "Part 1 = ", maxx - 1, maxy - 1, cmax
      
contains 

    function sum3x3 (g, x, y) result(s) 
        integer :: g(1:300,1:300), x, y, s, i, j

        s = 0
        do i = -1, 1
            do j = -1, 1
                s = s + g(x + i, y + j)
            end do
        end do 
    end function sum3x3
end program day11
