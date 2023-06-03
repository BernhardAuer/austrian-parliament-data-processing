namespace WebApi.Mappings;

// see https://www.parlament.gv.at/verstehen/glossare/abkuerzungen
public class AustrianParliamentAbbreviationMappings
{
    private Dictionary<string, string> SpeechTypes =>
        new()
        {
            { "c", "Contra"},
            { "p", "Pro"},
            { "el", "Erste Lesung"},
            { "rb", "Regierungsbank"},
            { "tb", "Tatsächliche Berichtigung"},
        };

    public string GetLongNameSpeechType(string abbreviation)
    {
        var isSuccessful = SpeechTypes.TryGetValue(abbreviation.ToLower(), out var longName);

        return (isSuccessful ? longName : abbreviation)!;
    }
    
}