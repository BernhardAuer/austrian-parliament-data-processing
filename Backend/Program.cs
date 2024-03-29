using WebApi.Infrastructure;
using WebApi.Mappings;
using WebApi.Models;
using WebApi.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.Configure<AustrianParliamentScrapeDatabaseSettings>(
    builder.Configuration.GetSection("AustrianParliamentScrapeDatabase"));

// cors has to be enabled for setups with different frontend/backend urls (so for local dev & PROD without reverse proxy)
builder.Services.AddCors();

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// register services // todo: check registrations...
builder.Services.AddSingleton<SpeechesMetaDataService>();
builder.Services.AddSingleton<NationalCouncilMeetingService>();
builder.Services.AddSingleton<AustrianParliamentAbbreviationMappings>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

var isCorsEnabled = builder.Configuration.GetValue<bool>("Cors:IsEnabledForProd");
if (isCorsEnabled)
{
    var corsAllowedHosts = builder.Configuration.GetSection("Cors:AllowedHosts")?.Get<List<string>>()?.ToArray() 
                           ?? Array.Empty<string>();
    app.UseCors(builder =>
    {
        builder.WithOrigins(corsAllowedHosts)
            .AllowAnyHeader()
            .AllowAnyMethod();
    });
}

app.UseCors();

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

MongoDbInit.CreateIndices(
    builder.Configuration.GetValue<string>("AustrianParliamentScrapeDatabase:ConnectionString"),
    builder.Configuration.GetValue<string>("AustrianParliamentScrapeDatabase:DatabaseName"),
    builder.Configuration.GetValue<string>("AustrianParliamentScrapeDatabase:SpeechesMetaDataCollectionName")
);

app.Run();

