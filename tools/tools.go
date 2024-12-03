package tools

import "os"

func LoadData(filename string) []byte {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic(err)
	}

	return data
}
