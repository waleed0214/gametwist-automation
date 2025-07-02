def compare_balances(ui_balance, api_balance):
    print(f"💻 UI Balance: {ui_balance}")
    print(f"🌐 API Balance: {api_balance}")
    if ui_balance == api_balance:
        print("✅ Balances match.")
    else:
        print(f"❌ Mismatch! UI: {ui_balance} vs API: {api_balance}")
