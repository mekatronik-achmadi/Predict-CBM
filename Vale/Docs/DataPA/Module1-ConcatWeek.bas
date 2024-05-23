Attribute VB_Name = "Module1"
Sub Merge_Multiple_Sheets_Row_Wise()

Dim Work_Sheets() As String
ReDim Work_Sheets(Sheets.Count)


For i = 0 To Sheets.Count - 1
    Work_Sheets(i) = Sheets(i + 1).Name
Next i

Sheets.Add.Name = "PA_Summary"

Dim Row_Index As Integer
Row_Index = Worksheets(1).UsedRange.Cells(1, 1).Row

Dim Column_Index As Integer
Column_Index = 0

For i = 0 To Sheets.Count - 2
    'Set Rng = Worksheets(Work_Sheets(i)).UsedRange
    Dim Rng As Range
    If i = 0 Then
        Set Rng = Worksheets(Work_Sheets(i)).Range(Worksheets(Work_Sheets(i)).Cells(3, 1), Worksheets(Work_Sheets(i)).Cells(17, 9))
    Else
        Set Rng = Worksheets(Work_Sheets(i)).Range(Worksheets(Work_Sheets(i)).Cells(3, 3), Worksheets(Work_Sheets(i)).Cells(17, 9))
    End If
    
    Worksheets(Work_Sheets(i)).Activate
    Rng.Copy
    Worksheets("PA_Summary").Cells(Row_Index, Column_Index + 1).PasteSpecial Paste:=xlPasteAllUsingSourceTheme
    
    If i = 0 Then
        Column_Index = Column_Index + 9
    Else
        Column_Index = Column_Index + 7
    End If
    
Next i

Application.CutCopyMode = False

End Sub

