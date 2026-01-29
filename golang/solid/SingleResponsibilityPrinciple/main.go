// Single Responsibility Principle (単一責任の原則)
// クラス（構造体）は単一の責任のみを持つべき
package main

import "fmt"

// [BAD] 悪い例: 複数の責任を持つ構造体
type BadUser struct {
	Name  string
	Email string
}

func (u *BadUser) Save() {
	// データベースに保存する責任
	fmt.Println("データベースに保存:", u.Name)
}

func (u *BadUser) SendEmail(message string) {
	// メール送信の責任
	fmt.Println("メール送信先:", u.Email, "内容:", message)
}

func (u *BadUser) GenerateReport() string {
	// レポート生成の責任
	return fmt.Sprintf("ユーザーレポート: %s (%s)", u.Name, u.Email)
}

// [GOOD] 良い例: 各責任を分離した設計

// User はユーザーデータのみを保持
type User struct {
	Name  string
	Email string
}

// UserRepository はユーザーの永続化を担当
type UserRepository struct{}

func (r *UserRepository) Save(u *User) {
	fmt.Println("データベースに保存:", u.Name)
}

func (r *UserRepository) FindByEmail(email string) *User {
	fmt.Println("メールアドレスで検索:", email)
	return &User{Name: "見つかったユーザー", Email: email}
}

// EmailService はメール送信を担当
type EmailService struct{}

func (s *EmailService) Send(to, message string) {
	fmt.Println("メール送信先:", to, "内容:", message)
}

// ReportGenerator はレポート生成を担当
type ReportGenerator struct{}

func (g *ReportGenerator) Generate(u *User) string {
	return fmt.Sprintf("ユーザーレポート: %s (%s)", u.Name, u.Email)
}

func main() {
	fmt.Println("=== 単一責任の原則 ===")
	fmt.Println()

	fmt.Println("[BAD] 悪い例: 1つの構造体が複数の責任を持つ")
	badUser := &BadUser{Name: "田中", Email: "tanaka@example.com"}
	badUser.Save()
	badUser.SendEmail("こんにちは")
	fmt.Println(badUser.GenerateReport())
	fmt.Println()

	fmt.Println("[GOOD] 良い例: 責任を分離")
	user := &User{Name: "佐藤", Email: "sato@example.com"}
	repo := &UserRepository{}
	emailService := &EmailService{}
	reportGen := &ReportGenerator{}

	repo.Save(user)
	emailService.Send(user.Email, "こんにちは")
	fmt.Println(reportGen.Generate(user))
}
