// Interface Segregation Principle (インターフェース分離の原則)
// クライアントは、使用しないメソッドへの依存を強制されるべきではない
// 大きなインターフェースより、小さく特化したインターフェースを使う
package main

import "fmt"

// [BAD] 悪い例: 巨大なインターフェース (Fat Interface)
type BadWorker interface {
	Work()
	Eat()
	Sleep()
	Code()
	Manage()
	Design()
}

// Robot は Eat, Sleep, Manage, Design を実装できない
type BadRobot struct {
	name string
}

func (r *BadRobot) Work() {
	fmt.Println(r.name, "が働いています")
}

func (r *BadRobot) Eat() {
	panic("ロボットは食べられません！") // ISP違反
}

func (r *BadRobot) Sleep() {
	panic("ロボットは寝ません！") // ISP違反
}

func (r *BadRobot) Code() {
	fmt.Println(r.name, "がコーディング中")
}

func (r *BadRobot) Manage() {
	panic("ロボットはマネジメントしません！") // ISP違反
}

func (r *BadRobot) Design() {
	panic("ロボットはデザインしません！") // ISP違反
}

// [GOOD] 良い例: 小さく分離されたインターフェース

// 基本的な能力ごとにインターフェースを分離
type Worker interface {
	Work()
}

type Eater interface {
	Eat()
}

type Sleeper interface {
	Sleep()
}

type Coder interface {
	Code()
}

type Manager interface {
	Manage()
}

type Designer interface {
	Design()
}

// 組み合わせたインターフェースも定義可能
type Human interface {
	Worker
	Eater
	Sleeper
}

type Developer interface {
	Worker
	Coder
}

// 人間の従業員
type HumanEmployee struct {
	name string
}

func (h *HumanEmployee) Work() {
	fmt.Println(h.name, "が働いています")
}

func (h *HumanEmployee) Eat() {
	fmt.Println(h.name, "がランチ中")
}

func (h *HumanEmployee) Sleep() {
	fmt.Println(h.name, "が休憩中")
}

func (h *HumanEmployee) Code() {
	fmt.Println(h.name, "がコーディング中")
}

// ロボット - 必要なインターフェースのみ実装
type Robot struct {
	name string
}

func (r *Robot) Work() {
	fmt.Println(r.name, "が働いています")
}

func (r *Robot) Code() {
	fmt.Println(r.name, "がコーディング中")
}

// マネージャー
type HumanManager struct {
	name string
}

func (m *HumanManager) Work() {
	fmt.Println(m.name, "が働いています")
}

func (m *HumanManager) Eat() {
	fmt.Println(m.name, "が会食中")
}

func (m *HumanManager) Sleep() {
	fmt.Println(m.name, "が休憩中")
}

func (m *HumanManager) Manage() {
	fmt.Println(m.name, "がチームを管理中")
}

// 必要な能力のみを要求する関数
func DoWork(w Worker) {
	w.Work()
}

func LunchBreak(e Eater) {
	e.Eat()
}

func DoCoding(c Coder) {
	c.Code()
}

func main() {
	fmt.Println("=== インターフェース分離の原則 ===")
	fmt.Println()

	fmt.Println("[BAD] 悪い例: 巨大インターフェースを実装")
	badRobot := &BadRobot{name: "BadBot"}
	badRobot.Work()
	badRobot.Code()
	// badRobot.Eat() // これを呼ぶとpanicになる
	fmt.Println("(Eat, Sleep, Manage, Design は実装できない)")
	fmt.Println()

	fmt.Println("[GOOD] 良い例: 分離されたインターフェース")
	human := &HumanEmployee{name: "田中"}
	robot := &Robot{name: "R2-D2"}
	manager := &HumanManager{name: "佐藤部長"}

	fmt.Println("-- 仕事 (Worker) --")
	workers := []Worker{human, robot, manager}
	for _, w := range workers {
		DoWork(w)
	}
	fmt.Println()

	fmt.Println("-- ランチ (Eater) --")
	eaters := []Eater{human, manager}
	for _, e := range eaters {
		LunchBreak(e)
	}
	fmt.Println("(ロボットはEaterではないので含まない)")
	fmt.Println()

	fmt.Println("-- コーディング (Coder) --")
	coders := []Coder{human, robot}
	for _, c := range coders {
		DoCoding(c)
	}
}
