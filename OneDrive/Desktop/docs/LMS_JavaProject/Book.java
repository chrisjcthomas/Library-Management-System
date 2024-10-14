
public class Book {
    private int bookId;
    private String title;
    private String author;
    private String genre;
    private boolean availabilityStatus;

    // Constructor
    public Book(int bookId, String title, String author, String genre, boolean availabilityStatus) {
        this.bookId = bookId;
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.availabilityStatus = availabilityStatus;
    }

    // Getters and Setters for each field
    public int getBookId() { return bookId; }
    public void setBookId(int bookId) { this.bookId = bookId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getAuthor() { return author; }
    public void setAuthor(String author) { this.author = author; }
    public String getGenre() { return genre; }
    public void setGenre(String genre) { this.genre = genre; }
    public boolean isAvailabilityStatus() { return availabilityStatus; }
    public void setAvailabilityStatus(boolean availabilityStatus) { this.availabilityStatus = availabilityStatus; }
    
    // Method to display book details
    public void displayBookDetails() {
        System.out.println("Book ID: " + bookId + ", Title: " + title + ", Author: " + author + ", Genre: " + genre + ", Available: " + availabilityStatus);
    }
}
