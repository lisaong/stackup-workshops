using Microsoft.EntityFrameworkCore;

namespace monit_hackernews.Data
{
    // Database context using Entity Framework
    // https://docs.microsoft.com/en-us/ef/core/get-started/?tabs=netcore-cli
    // https://elanderson.net/2019/11/asp-net-core-3-add-entity-framework-core-to-existing-project/    
    public class NewsHeadlineContext : DbContext
    {
        public NewsHeadlineContext(DbContextOptions<NewsHeadlineContext> options) : base(options)
        {}

        public DbSet<NewsHeadlineModel> Headlines { get; set; }
    }

    // Represents an entry in the database table
    public class NewsHeadlineModel
    {
        public int id { get; set; }

        public string title { get; set; }

        public string comment { get; set; }
    }
}