namespace converter2
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            buttonConvert = new Button();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            labelResult = new Label();
            comboBoxCategory = new ComboBox();
            comboBoxFromUnit = new ComboBox();
            comboBoxToUnit = new ComboBox();
            textBoxValue = new TextBox();
            label4 = new Label();
            SuspendLayout();
            // 
            // buttonConvert
            // 
            buttonConvert.Location = new Point(421, 257);
            buttonConvert.Name = "buttonConvert";
            buttonConvert.Size = new Size(162, 58);
            buttonConvert.TabIndex = 0;
            buttonConvert.Text = "Convert";
            buttonConvert.UseVisualStyleBackColor = true;
            buttonConvert.Click += buttonConvert_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(160, 36);
            label1.Name = "label1";
            label1.Size = new Size(122, 32);
            label1.TabIndex = 1;
            label1.Text = "Category: ";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(509, 102);
            label2.Name = "label2";
            label2.Size = new Size(51, 32);
            label2.TabIndex = 2;
            label2.Text = "To: ";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(160, 102);
            label3.Name = "label3";
            label3.Size = new Size(81, 32);
            label3.TabIndex = 3;
            label3.Text = "From: ";
            // 
            // labelResult
            // 
            labelResult.AutoSize = true;
            labelResult.Location = new Point(384, 367);
            labelResult.Name = "labelResult";
            labelResult.Size = new Size(255, 32);
            labelResult.TabIndex = 4;
            labelResult.Text = "Result will appear here";
            // 
            // comboBoxCategory
            // 
            comboBoxCategory.FormattingEnabled = true;
            comboBoxCategory.Location = new Point(275, 33);
            comboBoxCategory.Name = "comboBoxCategory";
            comboBoxCategory.Size = new Size(533, 40);
            comboBoxCategory.TabIndex = 5;
            comboBoxCategory.SelectedIndexChanged += comboBoxCategory_SelectedIndexChanged;
            // 
            // comboBoxFromUnit
            // 
            comboBoxFromUnit.FormattingEnabled = true;
            comboBoxFromUnit.Location = new Point(275, 102);
            comboBoxFromUnit.Name = "comboBoxFromUnit";
            comboBoxFromUnit.Size = new Size(224, 40);
            comboBoxFromUnit.TabIndex = 6;
            // 
            // comboBoxToUnit
            // 
            comboBoxToUnit.FormattingEnabled = true;
            comboBoxToUnit.Location = new Point(566, 102);
            comboBoxToUnit.Name = "comboBoxToUnit";
            comboBoxToUnit.Size = new Size(242, 40);
            comboBoxToUnit.TabIndex = 7;
            // 
            // textBoxValue
            // 
            textBoxValue.Location = new Point(275, 173);
            textBoxValue.Name = "textBoxValue";
            textBoxValue.Size = new Size(533, 39);
            textBoxValue.TabIndex = 8;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(160, 180);
            label4.Name = "label4";
            label4.Size = new Size(84, 32);
            label4.TabIndex = 9;
            label4.Text = "Value: ";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(13F, 32F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1023, 450);
            Controls.Add(label4);
            Controls.Add(textBoxValue);
            Controls.Add(comboBoxToUnit);
            Controls.Add(comboBoxFromUnit);
            Controls.Add(comboBoxCategory);
            Controls.Add(labelResult);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(buttonConvert);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button buttonConvert;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label labelResult;
        private ComboBox comboBoxCategory;
        private ComboBox comboBoxFromUnit;
        private ComboBox comboBoxToUnit;
        private TextBox textBoxValue;
        private Label label4;
    }
}
