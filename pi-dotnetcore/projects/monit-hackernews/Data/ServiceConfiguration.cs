
// https://www.stevebrownlee.com/asp-net-core-application-settings-in-razor/
namespace monit_hackernews.Data
{
    public interface IServiceConfiguration
    {
        string ThrottleIntervalMinutes { get; set; }

        string NewsServiceApiEndpointUri { get; set; }

        string NewsServiceUserUri { get; set; }

        string DatabaseName { get; set; }
    }

    public class ServiceConfiguration: IServiceConfiguration
    {
        public string ThrottleIntervalMinutes { get; set; }

        public string NewsServiceApiEndpointUri { get; set; }

        public string NewsServiceUserUri { get; set; }

        public string DatabaseName { get; set; }
    }
}