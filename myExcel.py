import openpyexcel

class MyExcel():
    def __init__(self, file_name):
        self.file_name = file_name
        self.wb = openpyexcel.load_workbook('Excel\\' + self.file_name)
        self.sheet = self.wb.get_sheet_by_name('Sayfa1')
    def __del__(self):
        self.wb.close()

    def create_personel_listesi(self, values):
        satir = 3
        sutun = 1
        for row_out in values:
            for column_out in row_out:
                self.sheet.cell(row=satir, column = sutun, value = column_out)
                if(len(row_out) == sutun):
                    sutun = 1
                    continue
                sutun += 1
            satir += 1
            

        self.wb.save('output\\' + self.file_name)
        print("Başarılı bir şekilde Excel dosyası oluşturuldu.")
