// Dependency Inversion Principle (依存性逆転の原則)
// 上位モジュールは下位モジュールに依存してはならない
// どちらも抽象（インターフェース）に依存すべき
package main

import "fmt"

// [BAD] 悪い例: 上位モジュールが下位モジュールの具体的な実装に依存

// 下位モジュール（具体的な実装）
type BadMySQLDatabase struct{}

func (db *BadMySQLDatabase) Save(data string) {
	fmt.Println("MySQLに保存:", data)
}

func (db *BadMySQLDatabase) Get(id int) string {
	return fmt.Sprintf("MySQLからID %d のデータを取得", id)
}

// 上位モジュール - MySQLに直接依存している
type BadUserService struct {
	db *BadMySQLDatabase // 具体的な実装に依存 (BAD)
}

func NewBadUserService() *BadUserService {
	return &BadUserService{
		db: &BadMySQLDatabase{}, // 具体的な実装を直接生成
	}
}

func (s *BadUserService) SaveUser(name string) {
	s.db.Save(name)
}

// PostgreSQLに変更したい場合、UserServiceのコードを修正する必要がある！

// [GOOD] 良い例: 抽象（インターフェース）に依存

// 抽象（インターフェース）- 上位・下位どちらも これに依存
type Database interface {
	Save(data string)
	Get(id int) string
}

// 下位モジュール - インターフェースを実装
type MySQLDatabase struct{}

func (db *MySQLDatabase) Save(data string) {
	fmt.Println("MySQLに保存:", data)
}

func (db *MySQLDatabase) Get(id int) string {
	return fmt.Sprintf("MySQLからID %d のデータを取得", id)
}

type PostgreSQLDatabase struct{}

func (db *PostgreSQLDatabase) Save(data string) {
	fmt.Println("PostgreSQLに保存:", data)
}

func (db *PostgreSQLDatabase) Get(id int) string {
	return fmt.Sprintf("PostgreSQLからID %d のデータを取得", id)
}

type InMemoryDatabase struct {
	data map[int]string
}

func NewInMemoryDatabase() *InMemoryDatabase {
	return &InMemoryDatabase{data: make(map[int]string)}
}

func (db *InMemoryDatabase) Save(data string) {
	id := len(db.data) + 1
	db.data[id] = data
	fmt.Println("メモリに保存:", data)
}

func (db *InMemoryDatabase) Get(id int) string {
	if data, ok := db.data[id]; ok {
		return fmt.Sprintf("メモリからID %d のデータを取得: %s", id, data)
	}
	return "データなし"
}

// 上位モジュール - インターフェースに依存
type UserService struct {
	db Database // インターフェースに依存 (GOOD)
}

// 依存性注入（Dependency Injection）
func NewUserService(db Database) *UserService {
	return &UserService{db: db}
}

func (s *UserService) SaveUser(name string) {
	s.db.Save(name)
}

func (s *UserService) GetUser(id int) string {
	return s.db.Get(id)
}

// 通知の例
type Notifier interface {
	Send(message string)
}

type EmailNotifier struct{}

func (n *EmailNotifier) Send(message string) {
	fmt.Println("メール送信:", message)
}

type SMSNotifier struct{}

func (n *SMSNotifier) Send(message string) {
	fmt.Println("SMS送信:", message)
}

type SlackNotifier struct{}

func (n *SlackNotifier) Send(message string) {
	fmt.Println("Slack送信:", message)
}

// 上位モジュール - Notifierインターフェースに依存
type OrderService struct {
	notifier Notifier
}

func NewOrderService(n Notifier) *OrderService {
	return &OrderService{notifier: n}
}

func (s *OrderService) PlaceOrder(item string) {
	fmt.Println("注文処理:", item)
	s.notifier.Send("注文完了: " + item)
}

func main() {
	fmt.Println("=== 依存性逆転の原則 ===")
	fmt.Println()

	fmt.Println("[BAD] 悪い例: 具体的な実装に依存")
	badService := NewBadUserService()
	badService.SaveUser("田中")
	fmt.Println("(PostgreSQLに変更するにはUserServiceのコード修正が必要)")
	fmt.Println()

	fmt.Println("[GOOD] 良い例: インターフェースに依存")

	fmt.Println("-- MySQLを使用 --")
	mysqlService := NewUserService(&MySQLDatabase{})
	mysqlService.SaveUser("佐藤")

	fmt.Println("-- PostgreSQLを使用 --")
	postgresService := NewUserService(&PostgreSQLDatabase{})
	postgresService.SaveUser("鈴木")

	fmt.Println("-- InMemoryを使用（テスト用） --")
	memoryDB := NewInMemoryDatabase()
	memoryService := NewUserService(memoryDB)
	memoryService.SaveUser("高橋")
	fmt.Println(memoryService.GetUser(1))
	fmt.Println()

	fmt.Println("[GOOD] 通知サービスの例")
	fmt.Println("-- メール通知 --")
	emailOrder := NewOrderService(&EmailNotifier{})
	emailOrder.PlaceOrder("商品A")

	fmt.Println("-- SMS通知 --")
	smsOrder := NewOrderService(&SMSNotifier{})
	smsOrder.PlaceOrder("商品B")

	fmt.Println("-- Slack通知 --")
	slackOrder := NewOrderService(&SlackNotifier{})
	slackOrder.PlaceOrder("商品C")
}
