//  main.m
//
//  Created by Christopher Wright on 2007.06.12.

#import <Foundation/Foundation.h>

@interface MyObject : NSObject
+(void)aMethod:(id)param;
@end

@implementation MyObject
+(void)aMethod:(id)param{
    int x;
    for(x=0;x<1000;++x)
    {
        printf("Object Thread says x is %i\n",x);
        //usleep(1);
    }
}
@end

int main(int argc, char *argv[])
{
    int x;
    [NSThread detachNewThreadSelector:@selector(aMethod:) toTarget:[MyObject class] withObject:nil];
    [NSThread detachNewThreadSelector:@selector(aMethod:) toTarget:[MyObject class] withObject:nil];
    [NSThread detachNewThreadSelector:@selector(aMethod:) toTarget:[MyObject class] withObject:nil];

    usleep(1);
    for(x=0;x<1000;++x)
    {
        printf("Main thread says x is %i\n",x);
        
    }

	return 0;
}