class Constants:
    def __init__(self):
        """Initialize constants with user input"""
        self.area = float(input("Enter area: "))
        self.frequency = float(input("Enter frequency (in Hz): "))
        self.temperature = float(input("Enter temperature: "))
        self.epsilon_r = float(input("Enter εr: "))
        self.Cox = float(input("Enter Cox: "))
        self.phi_m = float(input("Enter φm: "))
        self.chi = float(input("Enter χ: "))
        self.Eg = float(input("Enter Eg: "))
        self.semiconductor_type = input("Enter which type (n or p): ")
        self.epsilon_0 = 8.85418e-14  # Vacuum permittivity
        self.epsilon_s = self.epsilon_0 * self.epsilon_r  # Semiconductor permittivity

    def update_constants(self):
        """Allow user to update constants"""
        print("\nCurrent constants:")
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")

        if int(input("\nEnter 1 to change constants else 0: ")) != 1:
            return False

        while True:
            attr = input("Enter the name of the constant to change: ")
            if hasattr(self, attr):
                setattr(self, attr, float(input(f"Enter new value for {attr}: ")))
            else:
                print("Invalid constant name")

            if int(input("Any other constants to change? 1 if yes else 0: ")) != 1:
                break

        # Recalculate semiconductor permittivity
        self.epsilon_s = self.epsilon_0 * self.epsilon_r
        return True
