using System.Globalization;

namespace converter2
{
    public partial class Form1 : Form
    {
        private readonly Dictionary<string, Dictionary<string, decimal>> categories = new();

        public Form1()
        {
            InitializeComponent();
        }

        private void LoadCategoriesFromCsv(string filePath)
        {
            categories.Clear();

            var lines = File.ReadAllLines(filePath);

            for (int i = 1; i < lines.Length; i++)
            {
                var parts = lines[i].Split(',');

                var category = parts[0].Trim();
                var unit = parts[1].Trim();
                var factor = decimal.Parse(parts[2].Trim());

                if (!categories.ContainsKey(category))
                    categories[category] = new Dictionary<string, decimal>();

                categories[category][unit] = factor;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var filePath = Path.Combine(Application.StartupPath, "units.csv");
            LoadCategoriesFromCsv(filePath);

            comboBoxCategory.Items.Clear();

            foreach (var category in categories.Keys)
                comboBoxCategory.Items.Add(category);

            comboBoxCategory.SelectedIndex = 0;
        }


        private void comboBoxCategory_SelectedIndexChanged(object sender, EventArgs e)
        {
            var category = comboBoxCategory.SelectedItem.ToString();
            var units = categories[category];

            comboBoxFromUnit.Items.Clear();
            comboBoxToUnit.Items.Clear();

            foreach (var unit in units.Keys)
            {
                comboBoxFromUnit.Items.Add(unit);
                comboBoxToUnit.Items.Add(unit);
            }

            comboBoxFromUnit.SelectedIndex = 0;
            comboBoxToUnit.SelectedIndex = 1;
        }

        private void buttonConvert_Click(object sender, EventArgs e)
        {
            var value = decimal.Parse(textBoxValue.Text);
            var category = comboBoxCategory.SelectedItem.ToString();
            var fromUnit = comboBoxFromUnit.SelectedItem.ToString();
            var toUnit = comboBoxToUnit.SelectedItem.ToString();

            var result = value * categories[category][fromUnit] / categories[category][toUnit];

            labelResult.Text = $"{value} {fromUnit} = {result} {toUnit}";
        }
    }
}