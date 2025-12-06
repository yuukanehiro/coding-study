package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	lim := make(chan int, 2)
	var wg sync.WaitGroup

	fmt.Println("start")

	wg.Add(3)

	go func() {
		defer wg.Done()
		lim <- 1
		fmt.Println("job A start")
		time.Sleep(3 * time.Second)
		fmt.Println("job A end")
		<-lim
	}()

	go func() {
		defer wg.Done()
		lim <- 1
		fmt.Println("job B start")
		time.Sleep(3 * time.Second)
		fmt.Println("job B end")
		<-lim
	}()

	go func() {
		defer wg.Done()
		// limが2なので、ジョブA, Bで<-limで値が出力されるまでlimに値を入れられないので待つ
		lim <- 1
		fmt.Println("job C start")
		time.Sleep(3 * time.Second)
		fmt.Println("job C end")
		<-lim
	}()

	wg.Wait()
	fmt.Println("completed")
}

// Output:
// - 実行順は非決定的
// - LIFOっぽさがある

// % go run simple.go
// start
// job C start
// job A start
// job C end
// job B start
// job A end
// job B end
// completed

// % go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % GOMAXPROCS=1 go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed

// % GOMAXPROCS=1 go run simple.go
// start
// job C start
// job A start
// job A end
// job B start
// job C end
// job B end
// completed
