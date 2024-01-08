function formatDateTime() {
    const options = { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true };
    var currentDate = new Date()
    const formattedDateTime = currentDate.toLocaleString('en-US', options);
    document.getElementById('dateTime').textContent = formattedDateTime;
    var currentYear = currentDate.getFullYear();
    document.getElementById('currentYear').textContent = currentYear;
  }

  window.onload = formatDateTime;


  $(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > ($(document).height() - $(window).height()) * 0.9) {
      $('.navbar').addClass('scrolled');
      $('.navbar-light .navbar-brand').addClass('scrolled');
      $('.navbar-light .navbar-nav .active .nav-link').addClass('scrolled');
      $('.navbar-light .navbar-nav .nav-link').addClass('scrolled');
    } else {
      $('.navbar').removeClass('scrolled');
      $('.navbar-light .navbar-brand').removeClass('scrolled');
      $('.navbar-light .navbar-nav .active .nav-link').removeClass('scrolled');
      $('.navbar-light .navbar-nav .nav-link').removeClass('scrolled');

    }
  });
});

// popper effect

$(document).ready(function(){
    $('.list-item').popover({
        trigger: 'manual',
        animation: false    // Disable animation for immediate show/hide
    });

    // Show popover on mouseenter
    $('.list-item').on('mouseenter', function () {
        $(this).popover('show');
    });

    // Hide popover on mouseleave
    $('.list-item').on('mouseleave', function () {
        $(this).popover('hide');
    });
});

// curtain effect
// on click
    $(document).ready(function(){
        $('.list-item-cc').click(function() {
            var $description = $(this).find('.description');
            $description.toggle();
        });
    });


// on hover
    $(document).ready(function(){
    $('.list-item-c').click(

    function() {
        $(this).css('height', '200px');
    },
    function() {
       $(this).css('height', '25px');
    }
    );

    $('.list-item-cs').hover(
    function() {
        $(this).css('height', '100px');
    },
    function() {
        $(this).css('height', '25px');
    }
    );

    });
