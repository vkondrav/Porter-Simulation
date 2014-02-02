Public Class Main

    Private Sub numerals_KeyPress(ByVal sender As System.Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles Correct_Equipment.KeyPress, Patient_Readiness.KeyPress, Porter_Number.KeyPress
        If Not IsNumeric(e.KeyChar) And Not e.KeyChar = Convert.ToChar(Keys.Back) Then
            My.Computer.Audio.PlaySystemSound(Media.SystemSounds.Beep)
            e.Handled = True
        End If
    End Sub

    Private Sub ce_KeyPress(ByVal sender As System.Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles Porter_Wait_Time.KeyPress
        If e.KeyChar = "." And Porter_Wait_Time.Text.Contains(".") Then
            My.Computer.Audio.PlaySystemSound(Media.SystemSounds.Beep)
            e.Handled = True
        End If

        If Not IsNumeric(e.KeyChar) And Not e.KeyChar = Convert.ToChar(Keys.Back) And Not e.KeyChar = "." Then
            My.Computer.Audio.PlaySystemSound(Media.SystemSounds.Beep)
            e.Handled = True
        End If
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles fileBrowser.Click
        Dim dialog As New OpenFileDialog()

        dialog.Filter = "CSV Files (*.csv)|*csv"
        dialog.FilterIndex = 0

        If DialogResult.OK = dialog.ShowDialog Then
            File_Name.Text = dialog.FileName
        End If
    End Sub

    Private Sub Main_Load(sender As Object, e As EventArgs) Handles MyBase.Load, Reset_All.Click
        Porter_Number.Text = "10"
        Job_Distribution.SelectedIndex = 0
        Job_Intensity.SelectedIndex = 0
        Start_Date.Value = Today().AddDays(-1)
        End_Date.Value = Today().AddDays(-1)
        Correct_Equipment.Text = "80"
        Patient_Readiness.Text = "80"
        Porter_Wait_Time.Text = "5"
        File_Name.Text = ""
    End Sub

    Private Sub Simulate_Click(sender As Object, e As EventArgs) Handles Simulate.Click

        Dim err_str As String
        Dim go As Boolean

        go = True
        err_str = ""

        If (End_Date.Value < Start_Date.Value) Then
            go = False
            err_str += "End Date cannot be before the start date" & vbNewLine
        End If

        If (Convert.ToDecimal(Correct_Equipment.Text) > 100) Then
            go = False
            err_str += "Equipment Usage cannot be over 100%" & vbNewLine
        End If

        If (Convert.ToDecimal(Patient_Readiness.Text) > 100) Then
            go = False
            err_str += "Patient Readiness cannot be over 100%" & vbNewLine
        End If

        If Not My.Computer.FileSystem.FileExists(File_Name.Text) Then
            go = False
            err_str += "File does not exist" & vbNewLine
        End If

        If Not go Then
            MsgBox(err_str, , "Error")
        Else
            Shell("python C:\Users\Vitaliy\Documents\GitHub\Porter-Simulation\GUI\VS\Porter-Simulation\python\mockup.py", vbNormalFocus)
        End If

    End Sub
End Class
