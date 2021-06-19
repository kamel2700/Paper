#import <objc/objc.h>
#import <objc/Object.h>
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
    
		NSUInteger sizeOfArray = 10000;
		NSMutableArray *someArray = [NSMutableArray array];
		for (NSUInteger i = 0; i < sizeOfArray; i++) {
    		[someArray addObject:@(rand() % 1000)];
		} 
 
        // NSArray *quickSortData = @[@4, @3, @10, @44,@4444, @6, @4, @1, @7];
 
        
        [someArray sortUsingSelector:@selector(compare:)];
        // NSLog(@"Sorted Numbers %@", someArray);
 
    }
    return 0;
}