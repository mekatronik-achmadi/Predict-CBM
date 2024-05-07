Attribute VB_Name = "Module1"
Function ListComments(selectedRange As Range) As String
    Dim cell As Range
    Dim comment As comment
    Dim commentText As String
    
    For Each cell In selectedRange
        If Not cell.comment Is Nothing Then
            commentText = commentText & cell.comment.Text & vbCrLf
        End If
    Next cell
    
    If Len(commentText) > 0 Then
        ListComments = commentText
    Else
        ListComments = "No outages (Normal operation)."
    End If
End Function

