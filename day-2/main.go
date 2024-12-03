package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"git.thecodedom.com/aoc2024/tools"
)

type intSlice struct {
	number []int
}

func createSlices(data []byte) []intSlice {

	test := string(data)
	split := strings.Split(test, "\n")

	var numbers []intSlice

	for _, num := range split {
		if num != "" {

			var ints []int
			s := strings.Split(num, " ")
			for _, n := range s {
				t, err := strconv.Atoi(n)
				if err != nil {
					panic(err)
				}
				ints = append(ints, t)
			}
			numbers = append(numbers, intSlice{number: ints})

		}

	}

	return numbers
}

func (i intSlice) levelSafe() bool {
	var increasing bool = true

	currentLevel, temp := i.number[0], i.number[1:]
	i.number = temp

	if currentLevel > i.number[0] {
		increasing = false
	}

	for len(i.number) > 0 {
		difference := 0

		if increasing == true {
			if currentLevel > i.number[0] {
				return false
			}
			difference = currentLevel - i.number[0]
		} else {
			if currentLevel < i.number[0] {
				return false
			}
			difference = i.number[0] - currentLevel
		}

		if math.Abs(float64(difference)) == 0 || math.Abs(float64(difference)) > 3 {
			return false
		}

		currentLevel, temp = i.number[0], i.number[1:]
		i.number = temp

	}
	return true

}

func main() {
	d := tools.LoadData("input.txt")
	s := createSlices(d)

	var totalSafe int = 0

	for _, o := range s {
		r := o.levelSafe()

		if r {
			totalSafe += 1
		}
	}

	fmt.Println(totalSafe)
}
