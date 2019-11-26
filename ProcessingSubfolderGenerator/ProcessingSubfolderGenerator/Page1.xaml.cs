using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ProcessingSubfolderGenerator
{
    /// <summary>
    /// Interaction logic for Page1.xaml
    /// </summary>
    public partial class Page1 : Page
    {
        public Page1()
        {
            InitializeComponent();
        }

        private void ProcessingLocationButton_Click(object sender, RoutedEventArgs e)
        {
            FolderBrowserDialog temp = new FolderBrowserDialog();
            temp.ShowDialog();
            ProcessingSketchTxt.Text = temp.SelectedPath;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Frame pageFrame = null;
            DependencyObject currParent = VisualTreeHelper.GetParent(this);
            while (currParent != null && pageFrame == null)
            {
                pageFrame = currParent as Frame;
                currParent = VisualTreeHelper.GetParent(currParent);
            }

            // Change the page of the frame.
            if (pageFrame != null)
            {
                var temp = new Uri("Page2.xaml", UriKind.Relative);
                pageFrame.Source = temp;
                NavigationService.Navigate(temp, ProcessingSketchTxt.Text);
            }



        }
    }
}
