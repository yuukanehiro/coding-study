// Open/Closed Principle (開放閉鎖の原則)
// 拡張に対して開いており、修正に対して閉じているべき
package main

import "fmt"

// [BAD] 悪い例: 新しい図形を追加するたびに既存コードを修正する必要がある
type BadShape struct {
	Type   string
	Width  float64
	Height float64
	Radius float64
}

func BadCalculateArea(s BadShape) float64 {
	switch s.Type {
	case "rectangle":
		return s.Width * s.Height
	case "circle":
		return 3.14 * s.Radius * s.Radius
	// 新しい図形を追加するたびにここを修正...
	default:
		return 0
	}
}

// [GOOD] 良い例: インターフェースを使って拡張可能にする

// Shape インターフェース - 新しい図形はこれを実装するだけ
type Shape interface {
	Area() float64
	Name() string
}

// Rectangle 長方形
type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Name() string {
	return "長方形"
}

// Circle 円
type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return 3.14 * c.Radius * c.Radius
}

func (c Circle) Name() string {
	return "円"
}

// Triangle 三角形 - 既存コードを修正せずに追加できる！
type Triangle struct {
	Base   float64
	Height float64
}

func (t Triangle) Area() float64 {
	return t.Base * t.Height / 2
}

func (t Triangle) Name() string {
	return "三角形"
}

// AreaCalculator は Shape インターフェースに依存
// 新しい図形が追加されても、このコードは変更不要
type AreaCalculator struct{}

func (c *AreaCalculator) TotalArea(shapes []Shape) float64 {
	total := 0.0
	for _, shape := range shapes {
		total += shape.Area()
	}
	return total
}

func (c *AreaCalculator) PrintAreas(shapes []Shape) {
	for _, shape := range shapes {
		fmt.Printf("%s の面積: %.2f\n", shape.Name(), shape.Area())
	}
}

func main() {
	fmt.Println("=== 開放閉鎖の原則 ===")
	fmt.Println()

	fmt.Println("[BAD] 悪い例: switch文で型を判別")
	badRect := BadShape{Type: "rectangle", Width: 10, Height: 5}
	badCircle := BadShape{Type: "circle", Radius: 7}
	fmt.Printf("長方形の面積: %.2f\n", BadCalculateArea(badRect))
	fmt.Printf("円の面積: %.2f\n", BadCalculateArea(badCircle))
	fmt.Println()

	fmt.Println("[GOOD] 良い例: インターフェースで拡張可能に")
	shapes := []Shape{
		Rectangle{Width: 10, Height: 5},
		Circle{Radius: 7},
		Triangle{Base: 8, Height: 6}, // 新しい図形も簡単に追加
	}

	calculator := &AreaCalculator{}
	calculator.PrintAreas(shapes)
	fmt.Printf("合計面積: %.2f\n", calculator.TotalArea(shapes))
}
