package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func reverseStacks(stacks [9][]string) {
	for _, s := range stacks {
		for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
			s[i], s[j] = s[j], s[i]
		}
	}
}

func int10(s string) int64 {
	a, _ := strconv.ParseInt(s, 10, 0)
	return a
}

func main() {
	POS := map[int]int{
		2:  0,
		5:  1,
		9:  2,
		13: 3,
		17: 4,
		21: 5,
		25: 6,
		29: 7,
		33: 8,
	}

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var stacks [9][]string
	initStateFinished := false

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		str := scanner.Text()
		if !initStateFinished {
			if str == "" {
				initStateFinished = true
				reverseStacks(stacks)
			} else {
				for i, c := range str {
					if c != 32 && c != 91 && c != 93 {
						fmt.Println(i, POS[i], string(c))
						stacks[POS[i]] = append(stacks[POS[i]], string(c))
					}
				}
			}
		} else {
			fields := strings.Split(str, " ")
			cnt := int10(fields[1])
			from := int10(fields[3]) - 1
			to := int10(fields[5]) - 1
			fmt.Println(cnt, from, to)

			// part 1
			/*
				for i := int64(0); i < cnt; i++ {
					// pop value
					n := len(stacks[from]) - 1
					value := stacks[from][n]
					stacks[from] = stacks[from][:n]

					// push value
					stacks[to] = append(stacks[to], value)
				}
			*/
			// part 2
			low := len(stacks[from]) - int(cnt)
			values := stacks[from][low:]

			stacks[from] = stacks[from][:low]
			stacks[to] = append(stacks[to], values...)
		}
	}

	fmt.Println(stacks)

	for _, c := range stacks {
		n := len(c) - 1
		fmt.Print(c[n])
	}
	fmt.Println()
}
