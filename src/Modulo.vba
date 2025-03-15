Sub EnviarMensagensEmLote()
    Dim ultimaLinha As Integer
    Dim i As Integer
    Dim destinatario As String
    Dim mensagem As String
    Dim caminhoExe As String
    Dim shellCmd As String
    
    ' ?? Executável
    caminhoExe = ThisWorkbook.Path & "\dist\server.exe"

    ' ?? Números de telefone (+5544999999999)
    ultimaLinha = Cells(Rows.Count, 1).End(xlUp).Row

    ' ?? Percorrer a coluna A
    For i = 2 To ultimaLinha
        destinatario = Trim(Cells(i, 1).Value) 
        mensagem = Trim(Cells(i, 3).Value)

        ' ?? != vazio
        If destinatario <> "" And mensagem <> "" Then
            ' ?? Insnciar o executável
            shellCmd = caminhoExe & " """ & destinatario & """ """ & mensagem & """"

            ' ?? Enviar Msg
            Shell shellCmd, vbNormalFocus

            ' ?? Tempo de espera
            Application.Wait (Now + TimeValue("00:00:01"))

            ' ?? Registrar status no Excel
            Cells(i, 4).Value = "Enviado em " & Now()
        Else
            Cells(i, 4).Value = "? Erro: Dados inválidos!"
        End If
    Next i

    MsgBox "Mensagens processadas!", vbInformation
End Sub
