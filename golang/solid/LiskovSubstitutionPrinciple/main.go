// Liskov Substitution Principle (リスコフの置換原則)
// 派生型は基底型と置換可能でなければならない
// サブタイプは、そのスーパータイプの振る舞いを壊してはならない
package main

import "fmt"

// [BAD] 悪い例: 正方形は長方形のサブタイプとして不適切
// (数学的には正方形は長方形の一種だが、振る舞いが異なる)

type BadRectangle struct {
	width  float64
	height float64
}

func (r *BadRectangle) SetWidth(w float64) {
	r.width = w
}

func (r *BadRectangle) SetHeight(h float64) {
	r.height = h
}

func (r *BadRectangle) Area() float64 {
	return r.width * r.height
}

// BadSquare は BadRectangle を埋め込むが、振る舞いが異なる
type BadSquare struct {
	BadRectangle
}

func (s *BadSquare) SetWidth(w float64) {
	s.width = w
	s.height = w // 幅を設定すると高さも変わる！
}

func (s *BadSquare) SetHeight(h float64) {
	s.width = h // 高さを設定すると幅も変わる！
	s.height = h
}

// この関数は BadRectangle を期待しているが、BadSquare では予期しない動作になる
func BadResizeRectangle(r *BadRectangle) {
	r.SetWidth(5)
	r.SetHeight(10)
	// 期待: 面積 = 5 * 10 = 50
	// しかし BadSquare だと: 面積 = 10 * 10 = 100 (予期しない！)
	fmt.Printf("期待する面積: 50, 実際の面積: %.0f\n", r.Area())
}

// [GOOD] 良い例: 共通のインターフェースを使い、それぞれ独立した実装

// Shape インターフェース
type Shape interface {
	Area() float64
	Name() string
}

// Rectangle 長方形
type Rectangle struct {
	Width  float64
	Height float64
}

func NewRectangle(w, h float64) *Rectangle {
	return &Rectangle{Width: w, Height: h}
}

func (r *Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r *Rectangle) Name() string {
	return "長方形"
}

// Square 正方形 - 長方形とは独立した実装
type Square struct {
	Side float64
}

func NewSquare(side float64) *Square {
	return &Square{Side: side}
}

func (s *Square) Area() float64 {
	return s.Side * s.Side
}

func (s *Square) Name() string {
	return "正方形"
}

// PrintArea は Shape インターフェースを受け取る
// Rectangle でも Square でも正しく動作する
func PrintArea(s Shape) {
	fmt.Printf("%s の面積: %.2f\n", s.Name(), s.Area())
}

// Bird の例 - より分かりやすい例
// [BAD] 悪い例
type BadBird struct {
	Name string
}

func (b *BadBird) Fly() string {
	return b.Name + " が飛んでいます"
}

// ペンギンは鳥だが飛べない - LSP違反
type BadPenguin struct {
	BadBird
}

func (p *BadPenguin) Fly() string {
	panic("ペンギンは飛べません！") // 予期しない動作
}

// [GOOD] 良い例: 適切なインターフェース分離
type Bird interface {
	Move() string
	Name() string
}

type FlyingBird struct {
	name string
}

func (b *FlyingBird) Move() string {
	return b.name + " が飛んでいます"
}

func (b *FlyingBird) Name() string {
	return b.name
}

type Penguin struct {
	name string
}

func (p *Penguin) Move() string {
	return p.name + " が泳いでいます" // ペンギンは泳ぐ
}

func (p *Penguin) Name() string {
	return p.name
}

// どんな Bird でも正しく動作
func DescribeBird(b Bird) {
	fmt.Printf("%s: %s\n", b.Name(), b.Move())
}

func main() {
	fmt.Println("=== リスコフの置換原則 ===")
	fmt.Println()

	fmt.Println("[BAD] 悪い例: 正方形を長方形として扱う")
	rect := &BadRectangle{}
	fmt.Print("長方形: ")
	BadResizeRectangle(rect)

	square := &BadSquare{}
	fmt.Print("正方形: ")
	BadResizeRectangle(&square.BadRectangle)
	fmt.Println()

	fmt.Println("[GOOD] 良い例: インターフェースで統一")
	shapes := []Shape{
		NewRectangle(5, 10),
		NewSquare(7),
	}
	for _, s := range shapes {
		PrintArea(s)
	}
	fmt.Println()

	fmt.Println("[GOOD] 良い例: 鳥の例")
	birds := []Bird{
		&FlyingBird{name: "スズメ"},
		&FlyingBird{name: "ワシ"},
		&Penguin{name: "ペンギン"},
	}
	for _, b := range birds {
		DescribeBird(b)
	}
}
