package api

import (
	"github.com/Yelcde/microservices/order/internal/application/core/domain"
	"github.com/Yelcde/microservices/order/internal/ports"
)

// Estrutura atualizada para incluir a porta de pagamento
type Application struct {
	db      ports.DBPort
	payment ports.PaymentPort
}

// Função atualizada para aceitar o adaptador de pagamento
func NewApplication(db ports.DBPort, payment ports.PaymentPort) *Application {
	return &Application{
		db:      db,
		payment: payment,
	}
}

func (a Application) PlaceOrder(order domain.Order) (domain.Order, error) {
	err := a.db.Save(&order)
	if err != nil {
		return domain.Order{}, err
	}
	paymentErr := a.payment.Charge(&order)
	if paymentErr != nil {
		return domain.Order{}, paymentErr
	}
	return order, nil
}

func (a Application) Charge(ctx context.Context, payment domain.Payment) (domain.Payment, error) {
	if payment.TotalPrice > 1000 {
		return domain.Payment{}, status.Errorf(codes.InvalidArgument, "Payment over 1000 is not allowed.")
	}
	err := a.db.Save(ctx, &payment)
	if err != nil {
		return domain.Payment{}, err
	}
	return payment, nil
}

func (a Adapter) Create(ctx context.Context, request *payment.CreatePaymentRequest) (*payment.CreatePayment-Response, error) {
	log.WithContext(ctx).Info("Creating payment...")

	newPayment := domain.NewPayment(request.UserId, request.OrderId, request.TotalPrice)
	result, err := a.api.Charge(ctx, newPayment)
	code := status.Code(err)
	if code == codes.InvalidArgument {
		return nil, err
	} else if err != nil {
		return nil, status.New(codes.Internal, fmt.Sprintf("failed to charge. %v ", err)).Err()
	}
	ctx, _ := context.WithTimeout(context.Background(), 1*time.Second)
	return &payment.CreatePaymentResponse{PaymentId: result.ID}, nil
}