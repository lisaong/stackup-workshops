using Microsoft.EntityFrameworkCore;

namespace monit_hackernews.Data
{
    // Database context using Entity Framework
    // https://docs.microsoft.com/en-us/ef/core/get-started/?tabs=netcore-cli
    // https://hackernoon.com/asp-net-core-how-to-use-dependency-injection-in-entity-framework-core-4388fc5c148b
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