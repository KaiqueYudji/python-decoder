# commando to create an executable file: pyinstaller --onefile --add-binary "C:\Users\kaique\AppData\Local\Programs\Python\Python312:Dlls" decode_hexadecimal_packet.py


class Messages_decoder:

    def catching_the_value_of_each_entry(self, hexadecimal_package):
        incrementor: int = 0
        entry_values_in_hexa = []

        for position in range(len(hexadecimal_package)):
            entry_value = hexadecimal_package[incrementor: (incrementor + 8) ]
        

            if entry_value != '':
                entry_values_in_hexa.append(entry_value)
                incrementor = incrementor + 8
            else:
                break

        return entry_values_in_hexa



    def decoding_entry_value(self, entry_values_array_hexa):
        entry_values_decoded_array = []

        for entry_value in entry_values_array_hexa:
            
            data01 = int(entry_value[0:2], 16)
            data02 = int(entry_value[2:4], 16)
            data03 = int(entry_value[4:6], 16)
            data04 = int(entry_value[6:8], 16)

            entry_value_decoded = data01 + (data02 << 8) + (data03 << 16) + (data04 << 24)
            entry_values_decoded_array.append(entry_value_decoded)

        return entry_values_decoded_array   



    def pulsed_input_package_decoding(self, hexadecimal_package):
        data_of_packet = hexadecimal_package[50:len(hexadecimal_package)]
        entry_values_array_hexa = self.catching_the_value_of_each_entry(data_of_packet)
        entry_values_array_hexa.pop()#I need to do this because the last position of this array is the CRC of the packet

        entry_values_decoded = self.decoding_entry_value(entry_values_array_hexa)
        return entry_values_decoded



    def start(self):
        exit_program = "2"

        while exit_program == "2":
            decoded_value = self.pulsed_input_package_decoding(input("Digite o pacote bruto de dados enviados pelo telemetrix: "))
            port_position = 0

            print('\nEstes são os valores decodificados de acordo com as portas: ')
            for value in decoded_value:
                print(f'P{port_position}: {value}')
                port_position+=1

            exit_program = input("\nVocê deseja sair do programa? \n1 - Sim \n2 - Não\nDigite o número da sua resposta: ")
            if exit_program != "1" and exit_program != "2": print("\nEntrada inválida!"); break

        print("\nPrograma finalizado!")
        return


program =  Messages_decoder()
program.start()

