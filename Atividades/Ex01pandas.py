print(f'Dados faltantes:')
print(df.isnull().sum())

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y", errors='coerce')
print(f'Datas inválidas transformadas em NaT: {df["date"].isnull().sum()}')


print(f'Duplicatas: {df.duplicated().sum()}')
df = df.drop_duplicates()

print(f'Métodos de pagamento:')
payments_method = df['payment_method'].value_counts()
print(payments_method)

print(f'Resumo estatístico:')
print(df['value [USD]'].describe().round(2))

print(f'Vendidos por categoria:')
sales_category = df.groupby('product_category')['value [USD]'].sum().sort_values(ascending=False)
print(sales_category)

customer_spending = df.groupby('customer_id')['value [USD]'].sum().sort_values(ascending=False)
top_customer = customer_spending.head(10)
print(f'Top 10 clientes:')
print(top_customer)
