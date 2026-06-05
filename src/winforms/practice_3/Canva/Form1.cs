namespace Canva
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBoxCanvas_Paint(object sender, PaintEventArgs e)
        {
            var bluePen = new Pen(Color.Blue, 3);
            var brownPen = new Pen(Color.Brown, 5);
            var yellowPen = new Pen(Color.Yellow, 10);

            e.Graphics.DrawRectangle(brownPen, 150, 400, 500, 500);
            Point[] triangle =
            {
                new Point(100, 400),
                new Point(400, 150),
                new Point(700, 400)
            };

            e.Graphics.DrawPolygon(brownPen, triangle);
            e.Graphics.DrawEllipse(yellowPen, 700, 70, 200, 200);
            e.Graphics.DrawLine(bluePen, 0, 550, 150, 550);
            e.Graphics.DrawLine(bluePen, 650, 550, 1000, 550);
            e.Graphics.DrawIcon(SystemIcons.Question, 900, 900);
        }
    }
}
