using System.Windows;

namespace affute {
    /// <summary>
    ///     Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window {
        public static string currentPassword = "";

        public MainWindow() {
            InitializeComponent();
        }

        private void Button_OnClick(object sender, RoutedEventArgs e) {
            if (password.Text == "J3su1s@DM1n") {
                currentPassword = password.Text;
                var page = new AdminPage();
                Visibility = Visibility.Hidden;
                page.Show();
            }
        }
    }
}