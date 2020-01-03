using System;
using System.Drawing;
using System.Drawing.Imaging;

// Documentation: https://github.com/codebude/QRCoder
using QRCoder;

namespace hello_qrcoder
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            QRCodeGenerator qrGenerator = new QRCodeGenerator();
            QRCodeData qrCodeData = qrGenerator.CreateQrCode("The text which should be encoded.", 
                                        QRCodeGenerator.ECCLevel.Q);
            using (var qrCode = new QRCode(qrCodeData))
            {
                using (var qrCodeImage = qrCode.GetGraphic(20))
                {
                    qrCodeImage.Save("output.png", ImageFormat.Png);
                }
            }

            Console.WriteLine("Generated QRCode!");
        }
    }
}
