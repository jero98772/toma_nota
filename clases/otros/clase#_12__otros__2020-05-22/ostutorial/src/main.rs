#![no_std]
use core::panic::panicInfo
#[panic_handler]
fn panic(_info: &panicInfo)-> !{
	loop {}
}
fn main() {}
