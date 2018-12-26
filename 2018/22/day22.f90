program day22
    implicit none
    integer :: x,y,depth, i, j
    integer, allocatable :: geologic(:,:)
    integer, allocatable :: erosion(:,:)

    read(*,*) depth
    read(*,*) x,y

    allocate(geologic(0:x,0:y), erosion(0:x,0:y))

    geologic(0,0) = 0
    geologic(x,y) = 0

    do i = 0, x
        do j = 0, y
            if (i .eq. 0 .and. j .eq. 0) then
                geologic(0,0) = 0
            else if (i .eq. x .and. j .eq. y) then
                geologic(x,y) = 0 
            else if (i .eq. 0) then
                geologic(i,j) = 48271 * j
            else if (j .eq. 0) then
                geologic(i,j) = 16807 * i 
            else
                geologic(i,j) = geologic(i-1,j) * geologic(i,j-1) 
            end if

            geologic(i,j) = MOD(geologic(i,j) + depth, 20183)
            erosion(i,j) = MOD(geologic(i,j), 3)
        end do
    end do

    write(*,*) "Part 1: ", sum(erosion(:,:))
    
end program day22

