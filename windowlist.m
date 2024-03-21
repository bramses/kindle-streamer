////////////////////////////////////////////////////////////////////////////////
// windowlist.m
// Mark Setchell
//
// Get list of windows with their WindowOwnerNames, WindowNames and WindowNumbers
//
// Compile with:
// clang windowlist.m -o windowlist -framework coregraphics -framework cocoa
//
// Run with:
// ./windowlist
//
// You can then run "screencapture" to capture that window:
//
// screencapture -l<windowid> -x someFile.[png|jpg|tif]
////////////////////////////////////////////////////////////////////////////////
#include <Cocoa/Cocoa.h>
#include <CoreGraphics/CGWindow.h>

int main(int argc, char **argv)
{
   NSArray *windows = (NSArray *)CGWindowListCopyWindowInfo(kCGWindowListExcludeDesktopElements|kCGWindowListOptionOnScreenOnly,kCGNullWindowID);
   for(NSDictionary *window in windows){
      int WindowNum = [[window objectForKey:(NSString *)kCGWindowNumber] intValue];
      NSString* OwnerName = [window objectForKey:(NSString *)kCGWindowOwnerName];
      NSString* WindowName= [window objectForKey:(NSString *)kCGWindowName];
      printf("%s:%s:%d\n",[OwnerName UTF8String],[WindowName UTF8String],WindowNum);
   }
}