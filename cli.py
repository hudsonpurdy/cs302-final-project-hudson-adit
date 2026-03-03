from blockchain import Blockchain

def cli_loop():
    chain = Blockchain()

    while True:
        user_input = input("\n>>> ").strip().split()

        if not user_input:
            continue
        
        command = user_input[0].lower()
        args = user_input[1:]

        try:
            if command == "mint":
                owner = args[0]
                url = args[1]
                token = args[2]
                priv_key = args[3]
                
                chain.mint_nft(owner, url, token, priv_key)

            elif command == "block":
                try: 
                    sender = args[0]
                    receiver = args[1]
                    amount = args[2]
                    token = args[3] if len(args) > 3 else None
                    priv_key = args[4] if len(args) > 3 else None
                    
                    chain.add_block(sender, receiver, amount, token, priv_key)
                
                except Exception as e:
                    print(f"Error, try again. {e}")

            elif command == "add":
                username = args[0]

                chain.add_user(username)

            elif command == "get_user_nfts":
                username = args[0]

                chain.get_user_nfts(username)

            elif command == "print":
                chain.print_chain()

            elif command == "balances":
                chain.print_balances()

            elif command == "exit":
                print("Shutting down node...")
                break
            
            else:
                print(f"Unknown command: {command}")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    cli_loop()