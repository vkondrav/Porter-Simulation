<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Main
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Main))
        Me.Title = New System.Windows.Forms.Label()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.Job_Distribution = New System.Windows.Forms.ComboBox()
        Me.Job_Intensity = New System.Windows.Forms.ComboBox()
        Me.End_Date = New System.Windows.Forms.DateTimePicker()
        Me.Start_Date = New System.Windows.Forms.DateTimePicker()
        Me.Porter_Number = New System.Windows.Forms.TextBox()
        Me.ToolTip1 = New System.Windows.Forms.ToolTip(Me.components)
        Me.GroupBox2 = New System.Windows.Forms.GroupBox()
        Me.Label11 = New System.Windows.Forms.Label()
        Me.Label10 = New System.Windows.Forms.Label()
        Me.Porter_Wait_Time = New System.Windows.Forms.TextBox()
        Me.Patient_Readiness = New System.Windows.Forms.TextBox()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.Correct_Equipment = New System.Windows.Forms.TextBox()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.GroupBox3 = New System.Windows.Forms.GroupBox()
        Me.fileBrowser = New System.Windows.Forms.Button()
        Me.File_Name = New System.Windows.Forms.TextBox()
        Me.Label12 = New System.Windows.Forms.Label()
        Me.FolderBrowserDialog1 = New System.Windows.Forms.FolderBrowserDialog()
        Me.Advanced_Setting = New System.Windows.Forms.Button()
        Me.Reset_All = New System.Windows.Forms.Button()
        Me.Simulate = New System.Windows.Forms.Button()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.GroupBox1.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.GroupBox3.SuspendLayout()
        Me.SuspendLayout()
        '
        'Title
        '
        Me.Title.AutoSize = True
        Me.Title.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Title.Location = New System.Drawing.Point(12, 9)
        Me.Title.Name = "Title"
        Me.Title.Size = New System.Drawing.Size(344, 46)
        Me.Title.TabIndex = 0
        Me.Title.Text = "Porter Simulation"
        Me.Title.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.InitialImage = Nothing
        Me.PictureBox1.Location = New System.Drawing.Point(493, 12)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(291, 126)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        Me.PictureBox1.TabIndex = 1
        Me.PictureBox1.TabStop = False
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(6, 29)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(124, 17)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "Number of Porters"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(6, 64)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(72, 17)
        Me.Label2.TabIndex = 3
        Me.Label2.Text = "Start Date"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(6, 99)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(67, 17)
        Me.Label3.TabIndex = 4
        Me.Label3.Text = "End Date"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(6, 134)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(106, 17)
        Me.Label4.TabIndex = 5
        Me.Label4.Text = "Job Distribution"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(6, 169)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(87, 17)
        Me.Label5.TabIndex = 6
        Me.Label5.Text = "Job Intensity"
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.Job_Distribution)
        Me.GroupBox1.Controls.Add(Me.Job_Intensity)
        Me.GroupBox1.Controls.Add(Me.End_Date)
        Me.GroupBox1.Controls.Add(Me.Start_Date)
        Me.GroupBox1.Controls.Add(Me.Porter_Number)
        Me.GroupBox1.Controls.Add(Me.Label1)
        Me.GroupBox1.Controls.Add(Me.Label5)
        Me.GroupBox1.Controls.Add(Me.Label2)
        Me.GroupBox1.Controls.Add(Me.Label4)
        Me.GroupBox1.Controls.Add(Me.Label3)
        Me.GroupBox1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.GroupBox1.Font = New System.Drawing.Font("Microsoft Sans Serif", 7.8!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.GroupBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        Me.GroupBox1.Location = New System.Drawing.Point(20, 58)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(467, 197)
        Me.GroupBox1.TabIndex = 7
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Basic Settings"
        '
        'Job_Distribution
        '
        Me.Job_Distribution.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.Job_Distribution.FormattingEnabled = True
        Me.Job_Distribution.Items.AddRange(New Object() {"Data Based", "Poisson Distribution", "Lagrange Distribution"})
        Me.Job_Distribution.Location = New System.Drawing.Point(136, 134)
        Me.Job_Distribution.Name = "Job_Distribution"
        Me.Job_Distribution.Size = New System.Drawing.Size(200, 24)
        Me.Job_Distribution.TabIndex = 12
        '
        'Job_Intensity
        '
        Me.Job_Intensity.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.Job_Intensity.FormattingEnabled = True
        Me.Job_Intensity.Items.AddRange(New Object() {"Low", "Moderate", "High"})
        Me.Job_Intensity.Location = New System.Drawing.Point(136, 169)
        Me.Job_Intensity.Name = "Job_Intensity"
        Me.Job_Intensity.Size = New System.Drawing.Size(200, 24)
        Me.Job_Intensity.TabIndex = 11
        '
        'End_Date
        '
        Me.End_Date.Location = New System.Drawing.Point(136, 99)
        Me.End_Date.Name = "End_Date"
        Me.End_Date.Size = New System.Drawing.Size(200, 22)
        Me.End_Date.TabIndex = 9
        Me.ToolTip1.SetToolTip(Me.End_Date, "enter the end date of the statistical data to be used")
        '
        'Start_Date
        '
        Me.Start_Date.Location = New System.Drawing.Point(136, 64)
        Me.Start_Date.Name = "Start_Date"
        Me.Start_Date.Size = New System.Drawing.Size(200, 22)
        Me.Start_Date.TabIndex = 8
        Me.ToolTip1.SetToolTip(Me.Start_Date, "Input the start date for the statistical data to be used")
        '
        'Porter_Number
        '
        Me.Porter_Number.Location = New System.Drawing.Point(136, 29)
        Me.Porter_Number.Name = "Porter_Number"
        Me.Porter_Number.Size = New System.Drawing.Size(43, 22)
        Me.Porter_Number.TabIndex = 7
        Me.Porter_Number.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        Me.ToolTip1.SetToolTip(Me.Porter_Number, "Input Number of Porters")
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.Label11)
        Me.GroupBox2.Controls.Add(Me.Label10)
        Me.GroupBox2.Controls.Add(Me.Porter_Wait_Time)
        Me.GroupBox2.Controls.Add(Me.Patient_Readiness)
        Me.GroupBox2.Controls.Add(Me.Label9)
        Me.GroupBox2.Controls.Add(Me.Correct_Equipment)
        Me.GroupBox2.Controls.Add(Me.Label8)
        Me.GroupBox2.Controls.Add(Me.Label7)
        Me.GroupBox2.Controls.Add(Me.Label6)
        Me.GroupBox2.Location = New System.Drawing.Point(20, 262)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(467, 136)
        Me.GroupBox2.TabIndex = 8
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "Compliance"
        '
        'Label11
        '
        Me.Label11.AutoSize = True
        Me.Label11.Location = New System.Drawing.Point(263, 102)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(30, 17)
        Me.Label11.TabIndex = 11
        Me.Label11.Text = "min"
        '
        'Label10
        '
        Me.Label10.AutoSize = True
        Me.Label10.Location = New System.Drawing.Point(263, 68)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(20, 17)
        Me.Label10.TabIndex = 10
        Me.Label10.Text = "%"
        '
        'Porter_Wait_Time
        '
        Me.Porter_Wait_Time.Location = New System.Drawing.Point(185, 102)
        Me.Porter_Wait_Time.MaxLength = 10
        Me.Porter_Wait_Time.Name = "Porter_Wait_Time"
        Me.Porter_Wait_Time.Size = New System.Drawing.Size(72, 22)
        Me.Porter_Wait_Time.TabIndex = 9
        Me.Porter_Wait_Time.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Patient_Readiness
        '
        Me.Patient_Readiness.Location = New System.Drawing.Point(185, 68)
        Me.Patient_Readiness.MaxLength = 3
        Me.Patient_Readiness.Name = "Patient_Readiness"
        Me.Patient_Readiness.Size = New System.Drawing.Size(72, 22)
        Me.Patient_Readiness.TabIndex = 5
        Me.Patient_Readiness.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Location = New System.Drawing.Point(263, 37)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(20, 17)
        Me.Label9.TabIndex = 4
        Me.Label9.Text = "%"
        '
        'Correct_Equipment
        '
        Me.Correct_Equipment.Location = New System.Drawing.Point(185, 37)
        Me.Correct_Equipment.MaxLength = 3
        Me.Correct_Equipment.Name = "Correct_Equipment"
        Me.Correct_Equipment.Size = New System.Drawing.Size(72, 22)
        Me.Correct_Equipment.TabIndex = 3
        Me.Correct_Equipment.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Location = New System.Drawing.Point(9, 102)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(121, 17)
        Me.Label8.TabIndex = 2
        Me.Label8.Text = "Porter Wait Times"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Location = New System.Drawing.Point(9, 68)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(123, 17)
        Me.Label7.TabIndex = 1
        Me.Label7.Text = "Patient Readiness"
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(9, 34)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(170, 17)
        Me.Label6.TabIndex = 0
        Me.Label6.Text = "Correct Equipment Usage"
        '
        'GroupBox3
        '
        Me.GroupBox3.Controls.Add(Me.fileBrowser)
        Me.GroupBox3.Controls.Add(Me.File_Name)
        Me.GroupBox3.Controls.Add(Me.Label12)
        Me.GroupBox3.Location = New System.Drawing.Point(20, 405)
        Me.GroupBox3.Name = "GroupBox3"
        Me.GroupBox3.Size = New System.Drawing.Size(467, 81)
        Me.GroupBox3.TabIndex = 9
        Me.GroupBox3.TabStop = False
        Me.GroupBox3.Text = "Data Source"
        '
        'fileBrowser
        '
        Me.fileBrowser.Location = New System.Drawing.Point(430, 32)
        Me.fileBrowser.Name = "fileBrowser"
        Me.fileBrowser.Size = New System.Drawing.Size(30, 23)
        Me.fileBrowser.TabIndex = 2
        Me.fileBrowser.Text = "..."
        Me.fileBrowser.UseVisualStyleBackColor = True
        '
        'File_Name
        '
        Me.File_Name.Location = New System.Drawing.Point(107, 32)
        Me.File_Name.Name = "File_Name"
        Me.File_Name.Size = New System.Drawing.Size(317, 22)
        Me.File_Name.TabIndex = 1
        '
        'Label12
        '
        Me.Label12.AutoSize = True
        Me.Label12.Location = New System.Drawing.Point(12, 32)
        Me.Label12.Name = "Label12"
        Me.Label12.Size = New System.Drawing.Size(88, 17)
        Me.Label12.TabIndex = 0
        Me.Label12.Text = "File Location"
        '
        'Advanced_Setting
        '
        Me.Advanced_Setting.Location = New System.Drawing.Point(506, 276)
        Me.Advanced_Setting.Name = "Advanced_Setting"
        Me.Advanced_Setting.Size = New System.Drawing.Size(278, 56)
        Me.Advanced_Setting.TabIndex = 10
        Me.Advanced_Setting.Text = "Advanced Setting"
        Me.Advanced_Setting.UseVisualStyleBackColor = True
        '
        'Reset_All
        '
        Me.Reset_All.Location = New System.Drawing.Point(506, 338)
        Me.Reset_All.Name = "Reset_All"
        Me.Reset_All.Size = New System.Drawing.Size(278, 56)
        Me.Reset_All.TabIndex = 11
        Me.Reset_All.Text = "Reset All"
        Me.Reset_All.UseVisualStyleBackColor = True
        '
        'Simulate
        '
        Me.Simulate.Location = New System.Drawing.Point(506, 400)
        Me.Simulate.Name = "Simulate"
        Me.Simulate.Size = New System.Drawing.Size(278, 56)
        Me.Simulate.TabIndex = 12
        Me.Simulate.Text = "Simulate"
        Me.Simulate.UseVisualStyleBackColor = True
        '
        'Main
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(812, 491)
        Me.Controls.Add(Me.Simulate)
        Me.Controls.Add(Me.Reset_All)
        Me.Controls.Add(Me.Advanced_Setting)
        Me.Controls.Add(Me.GroupBox3)
        Me.Controls.Add(Me.GroupBox2)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.PictureBox1)
        Me.Controls.Add(Me.Title)
        Me.Name = "Main"
        Me.Text = "Main"
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.GroupBox2.ResumeLayout(False)
        Me.GroupBox2.PerformLayout()
        Me.GroupBox3.ResumeLayout(False)
        Me.GroupBox3.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Title As System.Windows.Forms.Label
    Friend WithEvents PictureBox1 As System.Windows.Forms.PictureBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents Job_Intensity As System.Windows.Forms.ComboBox
    Friend WithEvents End_Date As System.Windows.Forms.DateTimePicker
    Friend WithEvents Start_Date As System.Windows.Forms.DateTimePicker
    Friend WithEvents Porter_Number As System.Windows.Forms.TextBox
    Friend WithEvents ToolTip1 As System.Windows.Forms.ToolTip
    Friend WithEvents Job_Distribution As System.Windows.Forms.ComboBox
    Friend WithEvents GroupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents Correct_Equipment As System.Windows.Forms.TextBox
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents Porter_Wait_Time As System.Windows.Forms.TextBox
    Friend WithEvents Patient_Readiness As System.Windows.Forms.TextBox
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents GroupBox3 As System.Windows.Forms.GroupBox
    Friend WithEvents File_Name As System.Windows.Forms.TextBox
    Friend WithEvents Label12 As System.Windows.Forms.Label
    Friend WithEvents FolderBrowserDialog1 As System.Windows.Forms.FolderBrowserDialog
    Friend WithEvents fileBrowser As System.Windows.Forms.Button
    Friend WithEvents Advanced_Setting As System.Windows.Forms.Button
    Friend WithEvents Reset_All As System.Windows.Forms.Button
    Friend WithEvents Simulate As System.Windows.Forms.Button

End Class
