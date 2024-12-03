package main

import (
	"fmt"
	"strconv"
	"strings"

	"git.thecodedom.com/aoc2024/tools"
)

func createSlices(data []byte) string {

	test := string(data)
	split := strings.Split(test, "\n")

	var numbers []int

	newSplit := make([][]int, 0)
	for _, num := range split {
		fmt.Println(num)
		if num != "" {
			numbers = append([], strconv.Itoa(strings.Split(num, " ")))
			newSplit = append(newSplit, strings.Split(num, " "))
		}

	}
	lines := string(data)

	fmt.Println(newSplit)

	return lines
}

func main() {
	data := tools.LoadData("input_test.txt")

	createSlices(data)
}
