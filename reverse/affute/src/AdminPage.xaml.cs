using System;
using System.Windows;

namespace affute {
    public partial class AdminPage : Window {
        public AdminPage() {
            InitializeComponent();
            flag.Text = "AIRCTF{" + MainWindow.currentPassword + "}";
        }

        private void Window_OnClosed(object? sender, EventArgs e) {
            Application.Current.Shutdown();
        }
    }
}