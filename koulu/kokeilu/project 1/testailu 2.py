uusi_tulos = [(item[0], item[-1], self.risk + item[-1] / self.risk_kerroin) for item in tulos]
        table = PrettyTable()
        table.field_names = ["#", "Lentokentän nimi", "Etäisyys KM", "Riski jäädä kiinni %"]
        for i, row in enumerate(uusi_tulos):
            #lasketaan etäisyyden mukaan riski jokaiselle kentälle jäädä kiinni

            etäisyys = row[-1]
            risk = round((etäisyys / self.risk_kerroin) + self.risk, 2)
            table.add_row([i + 1] + list(row) + [risk])
